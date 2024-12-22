from customtkinter import CTkButton
from tkinter import colorchooser

def choose_color(master, widget: CTkButton):
    color = colorchooser.askcolor(parent=master, title='Choose a color')
    print(color)
    if color[1] is not None:
        widget.configure(fg_color=color[1])
        widget.configure(hover_color=color[1])
        if (0.2126*color[0][0]+0.7152*color[0][1]+0.0722*color[0][2]) > 128:
            widget.configure(text_color='#000000')
        else:
            widget.configure(text_color='#ffffff')
        return color[1]

def get_index_by_parameter(tab: list, parameter, value):
    return next((index for (index, d) in enumerate(tab) if d[parameter] == value), None)