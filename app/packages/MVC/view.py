import tkinter as tk
from tkinter import simpledialog, messagebox
import os

from packages.visuals.item_window import item_creator
from packages.utilities.save_functions import *
from packages.utilities.export import *
from packages.data.variables import *
from customtkinter import *

class View:
    """Interface utilisateur pour l'affichage et l'interaction"""
    def __init__(self, root: CTk, controller):
        self.root = root
        self.controller = controller

        self.dark_color_1 = "#1A1A1A"
        self.dark_color_2 = "#"
        self.gray_color_1 = "#6a6a6a"
        self.gray_color_2 = "#"
        self.light_blue_color = "#408ef2"
        self.dark_blue_color = "#2c63aa"
        self.whiteColor= '#eeeeee'

        self.root.title("Modustry")
        self.root.state("zoomed")
        self.root.geometry("640x480")
        self.root.resizable(False, False)
        set_appearance_mode('dark')

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
        self.root.after(250, lambda: self.root.iconbitmap(icon_path))


        # Menu frame
        root_bar = tk.Menu(self.root,font=CTkFont(size = 16))

        # File menu 
        file_menu = tk.Menu(root_bar, tearoff=0,font=CTkFont(size = 16))
        file_menu.add_command(label="Save file", command=save_file)
        file_menu.add_command(label="Load file", command=lambda: load_file(self.update_list(item_list,
                                                                                            liquid_list)))
        file_menu.add_command(label="Pack", command=lambda: mod_window(root))

        # Adding menu
        add_menu = tk.Menu(file_menu, tearoff=0,font=CTkFont(size = 16))
        add_menu.add_command(label="New Item", command = lambda: item_creator(root))

        root_bar.add_cascade(label="File", menu=file_menu)
        root_bar.add_cascade(label="Add", menu=add_menu)

        self.root.config(menu=root_bar)

        self.main_frame = CTkFrame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        ##### liste des items #####
        self.items_frame = CTkFrame(self.main_frame, fg_color=self.dark_color_1, border_color= self.whiteColor,border_width=2)
        self.items_frame.pack(side="left")

        self.items_label = CTkLabel(self.items_frame, text="Items",bg_color = self.dark_color_1,text_color = self.whiteColor,font=CTkFont(size = 30))
        self.items_label.pack(side="top", pady=5)

        self.item_listbox = tk.Listbox(self.items_frame, width=40, height=40, bg=self.dark_color_1, fg=self.whiteColor, highlightbackground= self.dark_color_1)
        self.item_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.item_listbox.bind("<<ListboxSelect>>", self.on_item_select)

        # Boutons
        self.buttons_frame = CTkFrame(self.main_frame, fg_color=self.dark_color_1, border_color= self.whiteColor,border_width=2)
        self.buttons_frame.pack(side="left", ipadx=20, padx = 20)

        self.add_item_button = CTkButton(self.buttons_frame, text="Add Item", command=self.controller.add_item,
                                    width= 120, height=40, fg_color=self.light_blue_color, hover_color=self.dark_blue_color,
                                    text_color=self.dark_color_1, font=CTkFont(size = 18))
        self.add_item_button.pack(pady=10)

        self.delete_item_button = CTkButton(self.buttons_frame, text="Delete Item", command=self.controller.delete_item,
                                    width= 120, height=40, fg_color=self.light_blue_color, hover_color=self.dark_blue_color,
                                    text_color=self.dark_color_1, font=CTkFont(size = 18))
        self.delete_item_button.pack(pady=10)
        
        ##### Liste des liquides #####
        self.liquids_frame = CTkFrame(self.main_frame, fg_color=self.dark_color_1, border_color= self.whiteColor,border_width=2)
        self.liquids_frame.pack(side="left")
        
        self.liquids_label = CTkLabel(self.liquids_frame, text="Liquids",bg_color = self.dark_color_1,text_color = self.whiteColor,font=CTkFont(size = 30))
        self.liquids_label.pack(side="top", pady=5)
        
        self.liquid_listbox = tk.Listbox(self.liquids_frame, width=40, height=40, bg=self.dark_color_1, fg=self.whiteColor, highlightbackground= self.dark_color_1)
        self.liquid_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.liquid_listbox.bind("<<ListboxSelect>>", self.on_liquid_select)
        
        self.add_liquid_button = CTkButton(self.buttons_frame, text="Add Liquid", command=self.controller.add_liquid,
                                    width= 120, height=40, fg_color=self.light_blue_color, hover_color=self.dark_blue_color,
                                    text_color=self.dark_color_1, font=CTkFont(size = 18))
        self.add_liquid_button.pack(pady=10)
        
        self.delete_liquid_button = CTkButton(self.buttons_frame, text="Delete Liquid", command=self.controller.delete_liquid,
                                    width= 120, height=40, fg_color=self.light_blue_color, hover_color=self.dark_blue_color,
                                    text_color=self.dark_color_1, font=CTkFont(size = 18))
        self.delete_liquid_button.pack(pady=10)



    def update_list(self, items, liquids):
        """Met à jour la liste"""
        if len(items) > 0:
            self.item_listbox.delete(0, tk.END)
        
        if len(liquids) > 0:
            self.liquid_listbox.delete(0, tk.END)
        
        for item in items:
            self.item_listbox.insert(tk.END, f"{item.name} - {item}")
        
        for liquid in liquids:
            self.liquid_listbox.insert(tk.END, f"{liquid.name} - {liquid}")
    
    ##### click selection #####
    def get_selected_item_index(self):
        """Retourne l'index de l'objet selectionné"""
        try:
            return self.item_listbox.curselection()[0]
        except IndexError:
            return None
    
    def get_selected_liquid_index(self):
        """Retourne l'index de l'objet selectionné"""
        try:
            return self.liquid_listbox.curselection()[0]
        except IndexError:
            return None
    
    ##### selection #####
    def on_item_select(self, event):
        """Notifie le controlleur qu'un objet est selectionné"""
        selected_item = self.item_listbox.curselection()
        if selected_item:
            self.controller.on_item_selected(selected_item[0])
    
    def on_liquid_select(self, event):
        """Notifie le controlleur qu'un liquide est selectionné"""
        selected_liquid = self.liquid_listbox.curselection()
        if selected_liquid:
            self.controller.on_liquid_selected(selected_liquid[0])