import tkinter as tk
from tkinter import simpledialog, messagebox
import os

from packages.visuals.item_window import item_creator
from packages.utilities.save_functions import *
from packages.utilities.export import *
from packages.data.variables import *
from customtkinter import *

from PIL import Image, ImageTk

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
        file_menu.add_command(label="Load file", command=lambda: load_file(self))
        file_menu.add_command(label="Pack", command=lambda: mod_window(root))

        # Adding menu
        # add_menu = tk.Menu(file_menu, tearoff=0,font=CTkFont(size = 16))
        # add_menu.add_command(label="New Item", command = lambda: item_creator(root))

        root_bar.add_cascade(label="File", menu=file_menu)
        # root_bar.add_cascade(label="Add", menu=add_menu)
        
        self.root.config(menu=root_bar)

        self.main_frame = CTkFrame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)



        ##### liste des items #####

        #initialize the lists needed in update_list()
        self.item_bin_buttons_list = []
        self.item_label_image_list = []
        self.item_texts_list = []


        self.items_frame = CTkFrame(self.main_frame, fg_color=self.dark_color_1, border_color= self.whiteColor,border_width=2)
        self.items_frame.pack(side="left", padx=10, pady=10)

        self.items_label = CTkLabel(self.items_frame, text="Items",bg_color = self.dark_color_1,text_color = self.whiteColor,font=("Arial", 30, "underline"))
        self.items_label.pack(side="top", pady=5)
        

        self.add_item_button = CTkButton(self.items_frame, text="Add Item", command=self.controller.add_item,
                                    width= 120, height=40, fg_color=self.light_blue_color, hover_color=self.dark_blue_color,
                                    text_color=self.dark_color_1, font=CTkFont(size = 18))
        self.add_item_button.pack(padx=23,pady=(20,10), anchor="w")


        self.item_canvas = tk.Canvas(self.items_frame, width=400, height=650, background=self.dark_color_1, highlightbackground=self.gray_color_1)
        self.item_canvas.pack(padx=(23, 0), pady=(0,23))

        self.item_scrollbar = CTkScrollbar(self.items_frame, orientation="vertical", command=self.item_canvas.yview, width = 15)
        self.item_scrollbar.pack(padx=2, pady=(0,15))
        self.item_scrollable_frame = tk.Frame(self.item_canvas, background=self.dark_color_1 )

        #bind the frame with the canvas
        self.item_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.item_canvas.configure(scrollregion=self.item_canvas.bbox("all"))
        )

        self.item_canvas.create_window((0, 0), window=self.item_scrollable_frame, anchor="nw")
        self.item_canvas.configure(yscrollcommand=self.item_scrollbar.set)

        self.item_canvas.pack(side="left", fill="both", expand=True)
        self.item_scrollbar.pack(side="right", fill="y") 



        ##### Liste des liquides #####

        self.liquids_bin_buttons_list = []
        self.liquids_label_image_list = []
        self.liquids_texts_list = []


        self.liquids_frame = CTkFrame(self.main_frame, fg_color=self.dark_color_1, border_color= self.whiteColor,border_width=2)
        self.liquids_frame.pack(side="right", padx=10, pady=10)

        self.liquids_label = CTkLabel(self.liquids_frame, text="Liquids",bg_color = self.dark_color_1,text_color = self.whiteColor,font=("Arial", 30, "underline"))
        self.liquids_label.pack(side="top", pady=5)
        

        self.add_liquid_button = CTkButton(self.liquids_frame, text="Add Liquid", command=self.controller.add_liquid,
                                    width= 120, height=40, fg_color=self.light_blue_color, hover_color=self.dark_blue_color,
                                    text_color=self.dark_color_1, font=CTkFont(size = 18))
        self.add_liquid_button.pack(padx=23,pady=(20,10), anchor="w")


        self.liquids_canvas = tk.Canvas(self.liquids_frame, width=400, height=650, background=self.dark_color_1, highlightbackground=self.gray_color_1)
        self.liquids_canvas.pack(padx=(23, 0), pady=(0,23))

        self.liquids_scrollbar = CTkScrollbar(self.liquids_frame, orientation="vertical", command=self.liquids_canvas.yview, width = 15)
        self.liquids_scrollbar.pack(padx=2, pady=(0,15))
        self.liquids_scrollable_frame = tk.Frame(self.liquids_canvas, background=self.dark_color_1 )

        #bind the frame with the canvas
        self.liquids_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.liquids_canvas.configure(scrollregion=self.liquids_canvas.bbox("all"))
        )

        self.liquids_canvas.create_window((0, 0), window=self.liquids_scrollable_frame, anchor="nw")
        self.liquids_canvas.configure(yscrollcommand=self.liquids_scrollbar.set)

        self.liquids_canvas.pack(side="left", fill="both", expand=True)
        self.liquids_scrollbar.pack(side="right", fill="y") 

    

    def update_list(self, element, items, liquids):
        """Met à jour les liste"""
        print(element,items,liquids)

        if element == "item":
            #reset lists
            for item_bin_button in self.item_bin_buttons_list:
                item_bin_button.destroy()
            for item_label_image in self.item_label_image_list:
                item_label_image.destroy()
            for item_text in self.item_texts_list:
                item_text.destroy()
            self.item_bin_buttons_list = []
            self.item_label_image_list = []
            self.item_texts_list = []

            self.item_images_list = []

            for i, item in enumerate(items):

                item_img = ImageTk.PhotoImage(Image.open(self.controller.items_image_paths[i]).resize((50, 50)))
                label_image = tk.Label(self.item_scrollable_frame, image=item_img)
                label_image.grid(row=i, column=0)
                self.item_label_image_list.append(label_image)
                self.item_images_list.append(item_img)  #just to remember the images else, they would be destroyed

                label_text = tk.Label(self.item_scrollable_frame, text=f"{item.name} - {item}",  background=self.dark_color_1, fg=self.whiteColor,font=CTkFont(size = 24))
                label_text.grid(row=i, column=1, padx=10, pady=5)
                self.item_texts_list.append(label_text)

                item_bin_button = CTkButton(self.item_scrollable_frame, command=lambda index=i: self.controller.delete_item(index),
                            width= 20, height=20, image=CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "..", "..", "icons", "bin_icon.png")), size=(30,30)),
                            bg_color=self.dark_color_1,fg_color=self.light_blue_color, text="",
                            hover_color=self.dark_blue_color)
                item_bin_button.grid(row=i, column=2,pady=5, padx = (5,0))
                self.item_bin_buttons_list.append(item_bin_button)
        
        elif element == "liquid":
            #reset lists
            for liquids_bin_button in self.liquids_bin_buttons_list:
                liquids_bin_button.destroy()
            for liquids_label_image in self.liquids_label_image_list:
                liquids_label_image.destroy()
            for liquids_text in self.liquids_texts_list:
                liquids_text.destroy()
            self.liquids_bin_buttons_list = []
            self.liquids_label_image_list = []
            self.liquids_texts_list = []

            self.liquids_images_list = []

            for i, liquid in enumerate(liquids):

                liquids_img = ImageTk.PhotoImage(Image.open(self.controller.liquids_image_paths[i]).resize((50, 50)))
                label_image = tk.Label(self.liquids_scrollable_frame, image=liquids_img)
                label_image.grid(row=i, column=0)
                self.liquids_label_image_list.append(label_image)
                self.liquids_images_list.append(liquids_img)  #just to remember the images else, they would be destroyed

                label_text = tk.Label(self.liquids_scrollable_frame, text=f"{liquid.name} - {liquid}",  background=self.dark_color_1, fg=self.whiteColor,font=CTkFont(size = 24))
                label_text.grid(row=i, column=1, padx=10, pady=5)
                self.liquids_texts_list.append(label_text)

                liquids_bin_button = CTkButton(self.liquids_scrollable_frame, command=lambda index=i: self.controller.delete_liquid(index),
                            width= 20, height=20, image=CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "..", "..", "icons", "bin_icon.png")), size=(30,30)),
                            bg_color=self.dark_color_1,fg_color=self.light_blue_color, text="",
                            hover_color=self.dark_blue_color)
                liquids_bin_button.grid(row=i, column=2,pady=5, padx = (5,0))
                self.liquids_bin_buttons_list.append(liquids_bin_button)
        
        elif element == "all":
            self.update_list("item", items, liquids)
            self.update_list("liquid", items, liquids)
    