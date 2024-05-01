import panel as pn
import pandas as pd
import numpy as np
import io
# from matplotlib.figure import Figure

ACCENT = "goldenrod"
LOGO = "https://assets.holoviz.org/panel/tutorials/matplotlib-logo.png"

pn.extension(design='material', sizing_mode="stretch_width")


# CONTENT =======================================================================================

markdown_text = """
# Sample Markdown Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed **sagittis** lacus nec **diam** facilisis, id *dapibus* justo *ultricies*. Fusce vel **odio** nec mauris eleifend vehicula. 

## Subheading

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sagittis lacus nec diam facilisis, id dapibus justo ultricies. Fusce vel odio nec mauris eleifend vehicula. 

### Sub-subheading

![Sample Image](https://via.placeholder.com/150)

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
- Sed sagittis lacus nec diam facilisis
- Fusce vel odio nec mauris eleifend vehicula

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Sed sagittis lacus nec diam facilisis
4. Fusce vel odio nec mauris eleifend vehicula

#### Sub-sub-subheading

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sagittis lacus nec diam facilisis, id dapibus justo ultricies. Fusce vel odio nec mauris eleifend vehicula. 

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sagittis lacus nec diam facilisis, id dapibus justo ultricies. Fusce vel odio nec mauris eleifend vehicula.

*Lorem ipsum* dolor sit amet, consectetur adipiscing elit. Sed sagittis lacus nec diam facilisis, id dapibus justo ultricies. Fusce vel odio nec mauris eleifend vehicula. 

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Sed sagittis lacus nec diam facilisis, id dapibus justo ultricies. Fusce vel odio nec m
"""

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
    name='this is the name of the dataframe'
)

# function to display a csv head when one is uploaded to file_input
# DOESNT WORK YET
def display_csv_head(event): 
    if isinstance(event.new, io.BytesIO):  # Check if we have the actual file data
        df = pd.read_csv(event.new)
        dataframe.value = df.head()

# binding the file_input widget to the function
# file_input.param.watch(display_csv_head, 'value')


# LAYOUT DISTRIBUTION OF ALL ELEMENTS =========================================================
pn.Row(
    introText,
    pn.Column(
        file_input,
        dataframe
    )
).servable()