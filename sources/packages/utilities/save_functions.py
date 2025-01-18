from __future__ import annotations
from typing import Optional
from tkinter import filedialog
from pickle import *

from ..data.variables import *

# Save method 
def save_file():
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
    global already_packed
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
        print(item_list)
        
        liquid_list.clear()
        liquid_list.extend(loaded_liquid_list)
        print(liquid_list)
        
        UC_list.clear()
        UC_list.extend(loaded_UC_list)
        print(UC_list)
        
        already_packed = loaded_already_packed
        print(already_packed)
        
        id_list.clear()
        id_list.extend(loaded_id_list)
        print(id_list)
        
        print("Mod loaded successfully!")
        
    else:
        print("no file was chosen")
    #callback() if callback else None

    # add image paths in controller from id list
    item_image_path = []
    liquid_image_path = []
    print(id_list)
    for dic in id_list:
        if(dic['element'] == "item"):
            item_image_path.append(dic['image_path'])
        else:
            liquid_image_path.append(dic['image_path'])

    view.controller.items_image_paths= item_image_path
    view.controller.liquids_image_paths= liquid_image_path

    view.update_list("all", item_list, liquid_list)

