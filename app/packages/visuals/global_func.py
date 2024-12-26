from customtkinter import CTkButton
from tkinter import colorchooser

def choose_color(master, widget: CTkButton):
    """
    Opens a color chooser dialog and applies the selected color to the given widget.

    Parameters:
    master (Tk): The parent window for the color chooser dialog.
    widget (CTkButton): The widget to which the selected color will be applied.

    Returns:
    str: The hexadecimal color code of the selected color, or None if no color was selected.

    The function performs the following actions:
    1. Opens a color chooser dialog.
    2. If a color is selected, it updates the widget's foreground color (fg_color) and hover color (hover_color).
    3. Adjusts the widget's text color (text_color) based on the brightness of the selected color to ensure readability.
    """
    color = colorchooser.askcolor(parent=master, title='Choose a color')
    if color[1] is not None:
        widget.configure(fg_color=color[1])
        widget.configure(hover_color=darken_hex_color(color[1], 0.2))
        if (0.2126*color[0][0]+0.7152*color[0][1]+0.0722*color[0][2]) > 128:
            widget.configure(text_color='#000000')
        else:
            widget.configure(text_color='#ffffff')
        return color[1]

def darken_hex_color(hex_color, factor=0.1):
    """
    Darken a hex color by a given factor.
    
    :param hex_color: The hex color string (e.g., "#408ef2").
    :param factor: The factor by which to darken the color (0.0 to 1.0).
    :return: The darkened hex color string.
    """
    # Ensure the hex color starts with '#'
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]

    # Convert hex color to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Darken the color by the factor
    r = int(r * (1 - factor))
    g = int(g * (1 - factor))
    b = int(b * (1 - factor))

    # Ensure the values are within the valid range
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Convert RGB back to hex
    darkened_hex_color = f"#{r:02x}{g:02x}{b:02x}"

    return darkened_hex_color
