from tkinter import messagebox
from .model import Model
from .view import View

from ..visuals.item_window import item_creator
from ..visuals.liquid_window import liquid_creator
from ..data.variables import *

class Controller:
    """Gère les interactions entre le modèle et la vue"""
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)
        
        self.selected_item = None
    
    ##### Item gestion #####
    def add_item(self):
        """Ajoute un nouvel objet"""
        def on_item_created(item, image_path):
            self.model.add_item(item, image_path)
            self.view.update_list(self.model.get_items())
        
        item_creator(self.view.root, on_item_created)

    def delete_item(self):
        index = self.view.get_selected_item_index()
        if index is not None:
            if confirm := messagebox.askyesno(
                "Delete this item ?", "Are you sure ?"
            ):
                self.model.remove_item(index)
                self.view.update_list(self.model.get_items())
    
    def on_item_selected(self, index):
        item = self.model.get_items()[index]
        self.selected_item = item
        print(f"selected Item: {item.name} - {item}")
    
    ##### Liquid gestion #####
    def add_liquid(self):
        """Ajoute un nouvel objet"""
        def on_liquid_created(liquid, image_path):
            self.model.add_liquid(liquid, image_path)
            self.view.update_list([], self.model.get_liquids())
        
        liquid_creator(self.view.root, on_liquid_created)
    
    def delete_liquid(self):
        index = self.view.get_selected_liquid_index()
        if index is not None:
            if confirm := messagebox.askyesno(
                "Delete this item ?", "Are you sure ?"
            ):
                self.model.remove_liquid()(index)
                self.view.update_list([], self.model.get_liquids())
    
    def on_liquid_selected(self, index):
        liquid = self.model.get_items()[index]
        self.selected_liquid = liquid
        print(f"selected Liquid: {liquid.name} - {liquid}")