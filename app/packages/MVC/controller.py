from .model import Model
from .view import View

from ..visuals.item_window import item_creator
from ..data.variables import *

class Controller:
    """Gère les interactions entre le modèle et la vue"""
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)
    
    def add_item(self):
        """Ajoute un nouvel objet"""
        item_creator()
        if type(item_list[-1])==Item:
            self.model.add_item(item_list[-1])
            self.view.update_list(self.model.get_items())
    
    def edit_item(self):
        pass