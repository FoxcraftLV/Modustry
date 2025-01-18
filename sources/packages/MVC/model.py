from ..data.mindustry_class.Item import Item
from ..data.mindustry_class.Liquid import Liquid
from ..data.variables import item_list, liquid_list, id_list

class Model:
    """Gestionnaire des objets"""
    def __init__(self) -> None:
        global item_list
    
    ##### Item gestion #####
    def add_item(self, item: Item, image_path: str) -> None:
        """Ajoute un nouvel item"""
        item_list.append(item)
        id_list.append({'name': item.name, 'item_id': item_list.index(item), 'image_path': image_path, 'element': "item"})

    def remove_item(self, index) -> None:
        """Supprime un item"""
        if 0 <= index < len(item_list):
            del item_list[index]
    
    def get_items(self) -> list:
        """Retourne la liste des items."""
        return item_list
    
    
    ##### Liquid gestion #####
    def add_liquid(self, liquid: Liquid, image_path: str) -> None:
        """Ajoute un nouvel item"""
        liquid_list.append(liquid)
        id_list.append({'name': liquid.name, 'item_id': liquid_list.index(liquid), 'image_path': image_path, 'element': "liquid"})

    def remove_liquid(self, index) -> None:
        """Supprime un item"""
        if 0 <= index < len(liquid_list):
            del liquid_list[index]
    
    def get_liquids(self) -> list:
        """Retourne la liste des items."""
        return liquid_list