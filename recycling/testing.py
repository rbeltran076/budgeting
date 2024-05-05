import panel as pn
import pandas as pd
import numpy as np
import openai
import io
import plotly.express as px

# SETUP
pn.extension(
    'plotly',
    'tabulator', 
    template='fast', 
    sizing_mode="stretch_width"
    )

pn.config.theme = 'dark'


# Set up your OpenAI API key
openai.api_key = '<KEY>'

# function to read any text from any txt file in the repo
def file_content(filename):
    try:
        with open(f"text/{filename}", "r") as file:
            # returning the content from the file
            return file.read()
    # Raise exception if not worked. 
    except FileNotFoundError:
        print("File not found.")
        return None


# CONTENT =======================================================================================

# set introText from the content from ./text/intro.txt 
introText = pn.pane.Markdown(file_content("intro.txt"))

# create a file input widget
file_input = pn.widgets.FileInput(accept='.csv')

# create a tabulator widget 
table = pn.widgets.Tabulator(
    pagination='remote',
    page_size=15, 
    sizing_mode='stretch_height',
    theme='fast'
    )

# create a Str pane
dataInfo = pn.pane.Str(styles={
    # CSS
    'font-size': '10pt',
    'color': '#f0f0f0',
    'background-color': '#181818',
    'padding': '15pt'
    }
)

dataInfo.object = "Waiting for a dataset to be uploaded\n\nAnytime now..."

# Create a Panel pane for the Plotly figure
plot_pane = pn.pane.Plotly(sizing_mode="stretch_both")


# LAYOUT DISTRIBUTION OF ALL ELEMENTS =========================================================
layout = pn.Row(
    pn.Column(
        introText,
        file_input
    ),
    pn.Tabs(
        ("Table", table),
        ("Info", dataInfo),
    )
)
layout.servable()
print("\n\n", layout, "\n")

# EVENT HANDLING =========================================================

# function to display a csv head when one is uploaded to file_input
def display_csv_head(event): 
    # print(event.new)  # fpd
    # Check if we have the actual file data
    if event.new:   
        print("\n\n\nNEW EVENT DETECTED\n\n") # fpd              
        # read the csv as 
        df = pd.read_csv(io.BytesIO(event.new))
        # print(df)  # fpd
        # Update the data attribute of dataframe
        table.value = df

# Bind the file_selector widget to the function
file_input.param.watch(display_csv_head, 'value')

def display_csv_info(event):
    if event.new:
        df = pd.read_csv(io.BytesIO(event.new))
        # Capture the output of df.info() as a string
        # NOTE: somewhere else in the script is another info variable
        # that is not equal to this.
        info = io.StringIO()
        df.info(buf=info)
        dataInfo.object = info.getvalue()

# Bind the file_selector widget to the function
file_input.param.watch(display_csv_info, 'value')

# # Create a sample Plotly figure
# df = px.data.iris()

# probably a good idea to make a py file with only this function
# then call it from here.
def generate_code(info):

    # AI persona from text file
    persona = f"""{file_content("persona.txt")}"""

    # AI prompt from text file
    prompt = f"""{file_content("prompt.txt").format(info=info)}"""

    # calling chat completion function and saving as 
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": prompt}],
        max_tokens=200,  
        n=1,
        stop=None
    )

    return completion.choices[0].message.content

# function to generate the plot with openai api
# i feel that is a tricky part
def generate_plot(event):
    info = dataInfo.object
    # print("\n\n", info)
    # call the function that uses the api
    code_snippet = generate_code(info)
    # execute the code generated (brackets bc usual format for gpt answers is ```python{code}```)
    # NOTE: This thing is basically like writing the new code in the editor and keep running it!!!

    # adding `display the generated plot` to the code_snippet
    print("\n", code_snippet, '\n')
    code_snippet += "\nplot_pane.object = fig\nlayout[0][0] = plot_pane"
    print("\n", code_snippet, '\n')

    # Execute the generated code snippet
    # allow using alongside all variables of this file
    exec(
        code_snippet, 
        globals(), locals()
        )
    
# Bind the file input widget to the generate_plot function
file_input.param.watch(generate_plot, 'value')