import panel as pn
import pandas as pd
import numpy as np
import io
from matplotlib.figure import Figure

ACCENT = "goldenrod"
LOGO = "https://assets.holoviz.org/panel/tutorials/matplotlib-logo.png"

pn.extension(design='material', sizing_mode="stretch_width")


# CONTENT========================

markdown_text = """
# Lorem Ipsum Dolor Sit Amet

Lorem ipsum dolor sit amet, consectetur adipiscing elit. **Sed do eiusmod tempor** incididunt ut labore et dolore magna aliqua. 

* Ut enim ad minim veniam
* Quis nostrud exercitation
* Ullamco laboris nisi ut aliquip ex ea commodo consequat

## Smaller Heading

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. _Excepteur sint occaecat_ cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

introText = pn.pane.Markdown(markdown_text)

# Create a file input widget
file_input = pn.widgets.FileInput(accept='.csv')

# create a dataframe widget 
dataframe = pn.widgets.DataFrame(
    pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
    }),
    name='this is the name of the dataframe',

)

# function to display a csv head when one is uploaded to file_input
def display_csv_head(event): 
    if isinstance(event.new, io.BytesIO):  # Check if we have the actual file data
        df = pd.read_csv(event.new)
        dataframe.value = df.head()

# binding the file_input widget to the function
file_input.param.watch(display_csv_head, 'value')

pn.Row(
    introText,
    pn.Column(
        file_input,
        dataframe
    )
).servable()
