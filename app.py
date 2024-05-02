import panel as pn
import pandas as pd
import numpy as np
import io
# from matplotlib.figure import Figure

# SETUP
pn.extension(
    'tabulator', 
    design='fast', 
    sizing_mode="stretch_width"
    )
pn.config.theme = 'dark'

# CONTENT =======================================================================================

# read the introText
with open('text/intro.txt', 'r') as file:
    introText = pn.pane.Markdown(file.read())
introText.style = {
    'font-size': '20px'
    }


# Create a file input widget
file_input = pn.widgets.FileInput(accept='.csv')

# create a tabulator widget 
table = pn.widgets.Tabulator(
    pagination='remote',
    page_size=15, 
    embed_content=True,
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

dataInfo.object = """Waiting for a dataset to be uploaded

Anytime now..."""


# FUNCTIONS FOR DYNAMIC APP FUNCTIONALITIES =========================================================

# function to display a csv head when one is uploaded to file_input
def display_csv_head(event): 
    print(event.new)  # fpd
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
        info = io.StringIO()
        df.info(buf=info)
        dataInfo.object = info.getvalue()

# Bind the file_selector widget to the function
file_input.param.watch(display_csv_info, 'value')


# LAYOUT DISTRIBUTION OF ALL ELEMENTS =========================================================
pn.Row(
    pn.Column(
        introText,
        file_input
    ),
    pn.Tabs(
        ("Table", table),
        ("Info", dataInfo),
    )
).servable()