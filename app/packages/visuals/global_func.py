from tkinter import Tk
from tkinter import colorchooser

def choose_color(master, widget: Tk):
    color = colorchooser.askcolor(parent=master, title='Choose a color')
    print(color)
    if color[1] is not None:
        widget.config(bg=color[1])
        if (0.2126*color[0][0]+0.7152*color[0][1]+0.0722*color[0][2]) > 128:
            widget.config(fg='#000000')
        else:
            widget.config(fg='#ffffff')
        return color[1]