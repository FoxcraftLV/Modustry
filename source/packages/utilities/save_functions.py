from __future__ import annotations
from typing import Optional
from tkinter import filedialog
from pickle import *

from ..data.variables import *

# Save method 
def save_file():
    """
    Opens a file dialog to save the current state of various lists to a file with a specified extension.
    The function prompts the user to select a file location and name using a save file dialog. 
    It then serializes and writes the contents of several lists (`item_list`, `liquid_list`, `UC_list`, 
    `already_packed`, and `id_list`) to the selected file in binary format.
    The file is saved with a default extension of ".modtry", but the user can choose from other 
    extensions such as ".minmod" or any other file type.
    The function prints a success message upon completion.
    Returns:
        None
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".modtry", filetypes=[("Mindustry Mod", "*.modtry"), ("Mindustry Mod", "*.minmod"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "wb") as file:
            dump(item_list, file)
            # print("items sauvegardés")
            dump(liquid_list, file)
            # print("liquides sauvegardés")
            dump(UC_list, file)
            # print("content sauv")
            dump(already_packed, file)
            # print("déjà pack")
            dump(id_list, file)
            # print("listes id sauv")
            
            file.close()
        print("Mod saved successfully!")

# load method 
def load_file(view):#callback: Optional[callable] = None):
    """
    Loads a mod file and updates the view with the loaded data.
    This function opens a file dialog to select a mod file with extensions .modtry, .minmod, or any file.
    It then loads the contents of the file, which include lists of items, liquids, unlockable content, 
    a boolean indicating if the mod is already packed, and a list of dictionaries containing IDs and image paths.
    The loaded data is used to update global variables and the view's controller.
    Args:
        view: The view object that will be updated with the loaded data.
    Returns:
        None
    """
    global already_packed, item_list, liquid_list, UC_list, id_list
    file_path = filedialog.askopenfilename(filetypes=[("Mindustry Mod", "*.modtry"), ("Mindustry Mod", "*.minmod"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "rb") as file:
            loaded_item_list: list[Item] = load(file)
            loaded_liquid_list: list[Liquid] = load(file)
            loaded_UC_list: list[UnlockableContent] = load(file)
            loaded_already_packed: bool = load(file)
            loaded_id_list: list[dict] = load(file)
            file.close()
        
        item_list.clear()
        item_list.extend(loaded_item_list)
        
        liquid_list.clear()
        liquid_list.extend(loaded_liquid_list)
        
        UC_list.clear()
        UC_list.extend(loaded_UC_list)
        
        already_packed = loaded_already_packed
        
        id_list.clear()
        id_list.extend(loaded_id_list)
        
        print("Mod loaded successfully!")
        
    else:
        print("no file was chosen")
    #callback() if callback else None

    # add image paths in controller from id list
    item_image_path = []
    liquid_image_path = []
    for dic in id_list:
        if(dic['element'] == "item"):
            item_image_path.append(dic['image_path'])
        else:
            liquid_image_path.append(dic['image_path'])

    view.controller.items_image_paths= item_image_path
    view.controller.liquids_image_paths= liquid_image_path

    view.update_list("all", item_list, liquid_list)

