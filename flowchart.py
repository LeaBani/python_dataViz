import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.sankey import Sankey

# Define the flowchart elements
elements = [
    "Start",
    "Initialize Variables",
    "Reference 'Input' Worksheet",
    "Disable ScreenUpdating & Calculation",
    "Loop Through Controls in UserForm2",
    "Get Control Name",
    "Is Control TextBox, ComboBox, ListBox, OptionButton, CheckBox?",
    "Build Range Name",
    "Get Control Value",
    "Does Range Exist in 'Input'?",
    "Display Error Message",
    "Is Control Value Not Empty?",
    "Is Control Value Numeric?",
    "Convert to Number & Assign to Cell",
    "Assign Value to Cell",
    "Re-enable ScreenUpdating & Calculation",
    "Hide UserForm2",
    "End"
]

# Create a figure for the flowchart
fig, ax = plt.subplots(figsize=(12, 10))

# Positioning of flowchart elements
positions = {
    "Start": (0.5, 0.95),
    "Initialize Variables": (0.5, 0.85),
    "Reference 'Input' Worksheet": (0.5, 0.75),
    "Disable ScreenUpdating & Calculation": (0.5, 0.65),
    "Loop Through Controls in UserForm2": (0.5, 0.55),
    "Get Control Name": (0.5, 0.45),
    "Is Control TextBox, ComboBox, ListBox, OptionButton, CheckBox?": (0.5, 0.35),
    "Build Range Name": (0.2, 0.25),
    "Get Control Value": (0.8, 0.25),
    "Does Range Exist in 'Input'?": (0.5, 0.2),
    "Display Error Message": (0.2, 0.1),
    "Is Control Value Not Empty?": (0.8, 0.1),
    "Is Control Value Numeric?": (0.5, 0.05),
    "Convert to Number & Assign to Cell": (0.2, -0.05),
    "Assign Value to Cell": (0.8, -0.05),
    "Re-enable ScreenUpdating & Calculation": (0.5, -0.2),
    "Hide UserForm2": (0.5, -0.3),
    "End": (0.5, -0.4),
}

# Create boxes for each element
for element, (x, y) in positions.items():
    ax.text(x, y, element, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue"))

# Define the flowchart connections
connections = [
    ("Start", "Initialize Variables"),
    ("Initialize Variables", "Reference 'Input' Worksheet"),
    ("Reference 'Input' Worksheet", "Disable ScreenUpdating & Calculation"),
    ("Disable ScreenUpdating & Calculation", "Loop Through Controls in UserForm2"),
    ("Loop Through Controls in UserForm2", "Get Control Name"),
    ("Get Control Name", "Is Control TextBox, ComboBox, ListBox, OptionButton, CheckBox?"),
    ("Is Control TextBox, ComboBox, ListBox, OptionButton, CheckBox?", "Build Range Name"),
    ("Is Control TextBox, ComboBox, ListBox, OptionButton, CheckBox?", "Get Control Value"),
    ("Build Range Name", "Does Range Exist in 'Input'?"),
    ("Get Control Value", "Does Range Exist in 'Input'?"),
    ("Does Range Exist in 'Input'?", "Display Error Message"),
    ("Does Range Exist in 'Input'?", "Is Control Value Not Empty?"),
    ("Is Control Value Not Empty?", "Is Control Value Numeric?"),
    ("Is Control Value Numeric?", "Convert to Number & Assign to Cell"),
    ("Is Control Value Numeric?", "Assign Value to Cell"),
    ("Convert to Number & Assign to Cell", "Re-enable ScreenUpdating & Calculation"),
    ("Assign Value to Cell", "Re-enable ScreenUpdating & Calculation"),
    ("Re-enable ScreenUpdating & Calculation", "Hide UserForm2"),
    ("Hide UserForm2", "End")
]

# Add arrows for each connection
for start, end in connections:
    start_x, start_y = positions[start]
    end_x, end_y = positions[end]
    ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                arrowprops=dict(facecolor='black', shrink=0.05, width=2))

# Remove axes
ax.axis('off')

# Display the flowchart
plt.show()
