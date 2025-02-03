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
    root = CTk()
    app = Controller(root)
    
    try:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
        icon_path = os.path.join(parent_dir, "icons\\main_ico.ico")
        if not os.path.isfile(icon_path):
            raise FileNotFoundError("Le fichier à l'emplacement {icon_path} n'existe pas.")
    except Exception:
        user = os.getlogin()
        icon_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Modustry\\data\\icons\\main_icon.ico"
        #self.root.iconbitmap(default=icon_path)
    
    root.after(250, lambda: root.iconbitmap(icon_path))

    root.mainloop()

if __name__ == "__main__":
    main()