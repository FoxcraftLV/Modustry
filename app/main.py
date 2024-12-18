import tkinter as tk
import os
from PIL import Image, ImageTk

from packages.visuals.item_window import item_creator
from packages.utilities.save_functions import *
from packages.utilities.export import *
from packages.data.variables import *

from packages.MVC.controller import Controller

# root = tk.Tk()
# root.title("Modustry")
# root.geometry("640x360")

# # some stuff for icon because else the software doen't work - don't ask me why
# #try:
# #    icon_path = os.path.join(os.path.dirname(__file__), "icons\\main_ico.ico")
# #    if not os.path.isfile(icon_path):
# #        raise FileNotFoundError("Le fichier à l'emplacement {icon_path} n'existe pas.")
# #except:
# #    user = os.getlogin()
# #    icon_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Modustry\\data\\icons\\main_icon.ico"

# icon_path = os.path.join(os.path.dirname(__file__), "icons", "main_ico.ico")
# icon_path = os.path.normpath(icon_path)
# root.iconbitmap(default=icon_path)

# # Menu frame
# root_bar = tk.Menu(root)

# # File menu 
# file_menu = tk.Menu(root_bar, tearoff=0)
# file_menu.add_command(label="Save file", command=save_file)
# file_menu.add_command(label="Load file", command=load_file)
# file_menu.add_command(label="Pack", command=lambda: mod_window(root))

# # Adding menu
# add_menu = tk.Menu(file_menu, tearoff=0)
# add_menu.add_command(label="New Item", command = lambda: item_creator(root))

# root_bar.add_cascade(label="File", menu=file_menu)
# root_bar.add_cascade(label="Add", menu=add_menu)

# root.config(menu=root_bar)

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()