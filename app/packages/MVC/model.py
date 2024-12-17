from ..data.mindustry_class.Item import Item

class Model:
    """Gestionnaire des objets"""
    def __init__(self) -> None:
        self.items: list = []
    
    ##### Item gestion #####
    def add_item(self, item: Item) -> None:
        """Ajoute un nouvel item"""
        self.items.append(item)
    
    def remove_item(self, index) -> None:
        """Supprime un item"""
        if 0 <= index < len(self.items):
            del self.items[index]
    
    def update_items(self, index, item: Item) -> None:
        """Modifie un item existant"""
        if 0 <= index < len(self.items):
            self.items[index] = item
    
    def get_items(self) -> list:
        """Retourne la liste des items."""
        return self.items