import tkinter as tk
from tkinter import simpledialog, messagebox

class View:
    """Interface utilisateur pour l'affichage et l'interaction"""
    def __init__(self, root: tk.Tk, controller):
        self.root = root
        self.controller = controller

        self.root.title("Modustry")
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)
        
        ##### liste des items #####
        self.item_listbox = tk.Listbox(self.main_frame, width=40, height=40)
        self.item_listbox.pack(side=tk.LEFT, padx=10)
        self.item_listbox.bind("<<ListboxSelect>>", self.on_item_select)
        
        # Boutons
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(side=tk.LEFT, padx=10)
        
        self.add_button = tk.Button(self.buttons_frame, text="Add Item", command=self.controller.edit_item)
        self.add_button.pack(pady=5)
        
        self.edit_button = tk.Button(self.buttons_frame, text="Edit Item", command=self.controller.edit_item)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete Item", command=self.controller.delete_item)
        self.delete_button.pack(pady=5)
    
    def update_list(self, items):
        """Met à jour la liste"""
        self.item_listbox.delete(0, tk.END)
        for item in items:
            self.item_listbox.insert(tk.END, f"{item.name} - {type(item)}")
    
    def get_selected_index(self):
        """Retourne l'index de l'objet selectionné"""
        try:
            return self.item_listbox.curselection()[0]
        except IndexError:
            return None
    
    def on_item_select(self, event):
        """Notifie le controlleur qu'un objet est selectionné"""
        self.controlleur.select_item()