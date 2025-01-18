import tkinter as tk
import os
from PIL import Image, ImageTk

from packages.visuals.item_window import item_creator
from packages.utilities.save_functions import *
from packages.utilities.export import *
from packages.data.variables import *
from customtkinter import *

from packages.MVC.controller import Controller

def main():
    root = CTk()
    app = Controller(root)

    root.mainloop()

if __name__ == "__main__":
    main()