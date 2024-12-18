from ..data.mindustry_class.Item import Item
from ..data.variables import item_list, id_list

class Model:
    """Gestionnaire des objets"""
    def __init__(self) -> None:
        global item_list
    
    ##### Item gestion #####
    def add_item(self, item: Item, image_path: str) -> None:
        """Ajoute un nouvel item"""
        item_list.append(item)
        id_list.append({'name': item.name, 'item_id': item_list.index(item), 'image_path': image_path})
    
    def remove_item(self, index) -> None:
        """Supprime un item"""
        if 0 <= index < len(item_list):
            del item_list[index]
    
    def update_items(self, index, item: Item) -> None:
        """Modifie un item existant"""
        if 0 <= index < len(item_list):
            item_list[index] = item
    
    def get_items(self) -> list:
        """Retourne la liste des items."""
        return item_list