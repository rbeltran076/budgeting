import panel as pn
import pandas as pd
import numpy as np
import io
# from matplotlib.figure import Figure

pn.extension('tabulator', design='material', sizing_mode="stretch_width")


# CONTENT =======================================================================================

# read the introText
with open('text/intro.txt', 'r') as file:
    introText = pn.pane.Markdown(file.read())

# Create a file input widget
file_input = pn.widgets.FileInput(accept='.csv')

# create a tabulator widget 
table = pn.widgets.Tabulator(pagination='remote', page_size=20, width=700, sizing_mode='stretch_height')
pn.widgets.Tabulator.theme = 'semantic-ui'

# create a Str pane
dataInfo = pn.pane.Str()
dataInfo.object = """Hello
This is me
"""


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
        info = str(df.info())
        print(info)
        dataInfo.object = f"""{df.info()}"""

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