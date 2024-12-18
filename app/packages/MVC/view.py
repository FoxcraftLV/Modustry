import tkinter as tk
from tkinter import simpledialog, messagebox
import os

from packages.visuals.item_window import item_creator
from packages.utilities.save_functions import *
from packages.utilities.export import *
from packages.data.variables import *

class View:
    """Interface utilisateur pour l'affichage et l'interaction"""
    def __init__(self, root: tk.Tk, controller):
        self.root = root
        self.controller = controller

        self.root.title("Modustry")
        self.root.geometry("640x360")

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
        
        self.root.iconbitmap(default=icon_path)

        # Menu frame
        root_bar = tk.Menu(self.root)

        # File menu 
        file_menu = tk.Menu(root_bar, tearoff=0)
        file_menu.add_command(label="Save file", command=save_file)
        file_menu.add_command(label="Load file", command=load_file)
        file_menu.add_command(label="Pack", command=lambda: mod_window(root))

        # Adding menu
        add_menu = tk.Menu(file_menu, tearoff=0)
        add_menu.add_command(label="New Item", command = lambda: item_creator(root))

        root_bar.add_cascade(label="File", menu=file_menu)
        root_bar.add_cascade(label="Add", menu=add_menu)

        self.root.config(menu=root_bar)


        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        ##### liste des items #####
        self.item_listbox = tk.Listbox(self.main_frame, width=40, height=40)
        self.item_listbox.pack(side=tk.LEFT, padx=10)
        self.item_listbox.bind("<<ListboxSelect>>", self.on_item_select)

        # Boutons
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.buttons_frame, text="Add Item", command=self.controller.add_item)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.buttons_frame, text="Edit Item", command=self.controller.edit_item)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete Item", command=self.controller.delete_item)
        self.delete_button.pack(pady=5)
    
    def update_list(self, items):
        """Met à jour la liste"""
        self.item_listbox.delete(0, tk.END)
        for item in items:
            self.item_listbox.insert(tk.END, f"{item.name} - {item}")
        print(item_list)
    
    def get_selected_index(self):
        """Retourne l'index de l'objet selectionné"""
        try:
            return self.item_listbox.curselection()[0]
        except IndexError:
            return None
    
    def on_item_select(self, event):
        """Notifie le controlleur qu'un objet est selectionné"""
        selected_item = self.item_listbox.curselection()
        if selected_item:
            self.controller.on_item_selected(selected_item[0])