import ipywidgets as widgets
from IPython.display import display

# Create the display screen
screen = widgets.Text(
    value='',
    placeholder='0',
    description='',
    disabled=True,
    layout=widgets.Layout(width='265px', height='50px')
)

# Function to handle button clicks
def on_button_clicked(b):
    current_value = screen.value
    button_label = b.description
    
    if button_label == "=":
        try:
            # eval() processes the string as a math equation
            screen.value = str(eval(current_value))
        except Exception:
            screen.value = "Error"
    elif button_label == "C":
        screen.value = ""
    else:
        screen.value = current_value + button_label

# Define button layout and style
button_layout = widgets.Layout(width='60px', height='60px', margin='2px')
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create button widgets and arrange them
rows = []
for row in buttons:
    button_row = []
    for label in row:
        btn = widgets.Button(description=label, layout=button_layout)
        # Apply special color to operators and clear button
        if label in ['/', '*', '-', '+', '=']:
            btn.style.button_color = 'orange'
        elif label == 'C':
            btn.style.button_color = 'lightcoral'
            
        btn.on_click(on_button_clicked)
        button_row.append(btn)
    rows.append(widgets.HBox(button_row))

# Display the calculator
calculator_vbox = widgets.VBox([screen] + rows)
display(calculator_vbox)
