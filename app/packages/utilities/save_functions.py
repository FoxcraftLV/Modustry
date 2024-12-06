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
            dump(UC_list, file)
            # print("content sauv")
            dump(already_packed, file)
            # print("déjà pack")
            dump(id_list, file)
            # print("listes id sauv")
            
            file.close()
        print("Mod saved successfully!")

# load method 
def load_file():
    global already_packed
    file_path = filedialog.askopenfilename(filetypes=[("Mindustry Mod", "*.modtry"), ("Mindustry Mod", "*.minmod"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "rb") as file:
            loaded_item_list: list[Item] = load(file)
            loaded_UC_list: list[UnlockableContent] = load(file)
            loaded_already_packed: bool = load(file)
            loaded_id_list: list[dict] = load(file)
            file.close()
        
        item_list.clear()
        item_list.extend(loaded_item_list)
        
        UC_list.clear()
        UC_list.extend(loaded_UC_list)
        
        already_packed = loaded_already_packed
        
        id_list.clear()
        id_list.extend(loaded_id_list)
        
        print("Mod loaded successfully!")
        return True
    else:
        print("no file was chosen")

