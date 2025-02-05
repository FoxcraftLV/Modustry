from tkinter import messagebox

from .model import Model
from .view import View

from ..visuals.item_window import item_creator
from ..visuals.liquid_window import liquid_creator
from ..data.variables import *


class Controller:
    """
    The Controller class is responsible for managing the interaction between the Model and the View.
    It handles user inputs and updates the View accordingly.
    Attributes:
        model (Model): The model instance that holds the data.
        view (View): The view instance that displays the data.
        selected_item (Item): The currently selected item.
        items_image_paths (list): A list of image paths for items.
        liquids_image_paths (list): A list of image paths for liquids.
    Methods:
        add_item():
            Adds a new item to the model and updates the view.
        delete_item(index):
            Deletes an item from the model and updates the view.
        on_item_selected(index):
            Handles the selection of an item and updates the selected_item attribute.
        add_liquid():
            Adds a new liquid to the model and updates the view.
        delete_liquid(index):
            Deletes a liquid from the model and updates the view.
    """
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)
        
        self.selected_item = None

        self.items_image_paths = []
        self.liquids_image_paths = []
    
    ##### Item gestion #####
    def add_item(self):
        def on_item_created(item, image_path):
            self.items_image_paths.append(image_path)
            self.model.add_item(item, image_path)
            self.view.update_list("item",self.model.get_items(), self.model.get_liquids())
        
        item_creator(self.view.root, on_item_created)

    def delete_item(self, index):
        if index is not None:
            if confirm := messagebox.askyesno(
                "Delete this item ?", "Are you sure ?"
            ):
                self.model.remove_item(index)
                del self.items_image_paths[index]
                self.view.update_list("item",self.model.get_items(), self.model.get_liquids())
    
    def on_item_selected(self, index):
        item = self.model.get_items()[index]
        self.selected_item = item
        print(f"selected Item: {item.name} - {item}")
    
    ##### Liquid gestion #####
    def add_liquid(self):
        def on_liquid_created(liquid, image_path):
            self.liquids_image_paths.append(image_path)
            self.model.add_liquid(liquid, image_path)
            self.view.update_list("liquid",self.model.get_items(), self.model.get_liquids())
        
        liquid_creator(self.view.root, on_liquid_created)
    
    def delete_liquid(self, index):
        if index is not None:
            if confirm := messagebox.askyesno(
                "Delete this item ?", "Are you sure ?"
            ):
                self.model.remove_liquid(index)
                del self.liquids_image_paths[index]

                self.view.update_list("liquid",self.model.get_items(), self.model.get_liquids())
    
