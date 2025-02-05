import tkinter as tk
from customtkinter import *
import os
from PIL import Image, ImageTk

from packages.visuals.item_window import item_creator
from packages.utilities.save_functions import *
from packages.utilities.export import *
from packages.data.variables import *

from packages.MVC.controller import Controller

def main():
    """
    The main function that initializes the application.
    This function creates an instance of the CTk class, initializes the
    Controller with the root window, and starts the main event loop.
    """
    root = CTk()
    app = Controller(root)

    root.mainloop()

if __name__ == "__main__":
    main()