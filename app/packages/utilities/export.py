from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from customtkinter import *
from pickle import *
import os
import shutil

from packages.visuals.item_window import create_hjson_item_file
from packages.visuals.liquid_window import create_hjson_liquid_file
from packages.data.variables import *

def mod_window(root):
    """
    Creates a new Toplevel window for entering mod parameters.
    Args:
        root (Tk): The root window or parent window.
    The window includes the following fields:
        - Identification Name: Entry for the mod's identification name.
        - Name in-game: Entry for the mod's display name in the game.
        - Author: Entry for the author's name.
        - Description: Text widget for the mod's description with a vertical scrollbar.
        - Minimum version: Entry for the minimum game version required.
        - Hidden: Checkbutton to mark the mod as hidden.
    A 'Create the mod' button is provided to pack all the entered information into a mod.
    """
    window = Toplevel(root)
    window.title('Mod parameters')
    # window.iconbitmap('D:\\project_2M_HUD_ui\\logo.ico')
    
    name = StringVar()
    displayName = StringVar()
    author = StringVar()
    minGameVersion = StringVar()
    # dependencies
    hidden = StringVar(value='false')
    
    # name
    name_box = LabelFrame(window, bg = '')
    name_box.pack(side='top', anchor='n')
    name_Label = Label(name_box, text='Identification Name :')
    name_Entry = Entry(name_box, textvariable=name)
    name_Label.pack(side='left')
    name_Entry.pack(side='left')
    
    # displayName
    displayName_box = LabelFrame(window, bg = '')
    displayName_box.pack(side='top', anchor='n')
    displayName_Label = Label(displayName_box, text='Name in-game :')
    displayName_Entry = Entry(displayName_box, textvariable=displayName)
    displayName_Label.pack(side='left')
    displayName_Entry.pack(side='left')
    
    # author
    author_box = LabelFrame(window, bg='')
    author_box.pack(side='top', anchor='n')
    author_Label = Label(author_box, text='Author :')
    author_Entry = Entry(author_box, textvariable=author)
    author_Label.pack(side='left')
    author_Entry.pack(side='left')
    
    # description
    description_box = LabelFrame(window, bg='')
    description_box.pack(side='top', anchor='n')
    description_Label = Label(description_box, text='Description :')
    description_Text = Text(description_box, height=5, width=20)
    description_Label.pack(side='left')
    description_Text.pack(side='left')
    description_Scrollbar = Scrollbar(description_box, orient=VERTICAL, command=description_Text.yview)
    description_Scrollbar.pack(side='left')
    
    # minGameVersion
    minGameVersion_box = LabelFrame(window, bg='')
    minGameVersion_box.pack(side='top', anchor='n')
    minGameVersion_Label = Label(minGameVersion_box, text='Minimun version :')
    minGameVersion_Entry = Entry(minGameVersion_box, textvariable=minGameVersion)
    minGameVersion_Label.pack(side='left')
    minGameVersion_Entry.pack(side='left')
    
    # hidden
    hidden_Check = Checkbutton(window, text='is hidden', variable=hidden, offvalue="false", onvalue="true")
    hidden_Check.pack(side='top', anchor='n')
    
    create_button = Button(window, text='Create the mod', command=lambda: pack_all(window, name.get(), displayName.get(), author.get(), description_Text.get('1.0', 'end-1c'), minGameVersion.get(), hidden.get()))
    
    create_button.pack(side='top', anchor='n')
    
    window.pack_propagate()

# TODO: Optimize file writing to reduce I/O operations and improve performance
# FIXME: Improve error handling for file operations
def pack_all(root, name, displayName, author, description, minGameVersion, hidden):
    """
    Packs all items and creates necessary files for a mod.
    Args:
        name (str): The name of the mod.
        displayName (str): The display name of the mod.
        author (str): The author of the mod.
        description (str): The description of the mod.
        minGameVersion (str): The minimum game version required for the mod. Defaults to "136" if empty.
        hidden (bool): Whether the mod is hidden or not.
    Returns:
        None
    """
    global already_packed, item_list, id_list, UC_list
    if not already_packed:
        file_path = filedialog.askdirectory(title="Select directory to save items")
        create_folder(file_path)
        already_packed = True
    os.chdir(file_path)
    
    progress = ttk.Progressbar(orient = HORIZONTAL, length = 100, mode = 'determinate')
    progress.pack(side='top', anchor='n')
    root.update_idletasks()
    
    total_files = len(item_list) + len(liquid_list)
    progress["maximum"] = total_files
    progress["value"] = 0

    if(minGameVersion == ""):
        minGameVersion = "136"

    mod_text = f"""
    {{
        'name': '{name}',
        'displayName': '{displayName}',
        'author': '{author}',
        'description': '{description}',
        'minGameVersion': {minGameVersion},
        'hidden': {hidden}
    }}
    """
    with open('mod.hjson', 'w') as file:
        file.write(mod_text)
        file.close()
        progress["value"] += 1
    
    if item_list:
        os.chdir("content")
        os.chdir("items")
        for item in item_list:
            for id in id_list:
                if item.name == id['name']:
                    hjson = create_hjson_item_file(item)
                    shutil.copy(id['image_path'],  os.path.join(file_path, "sprites/items"))
                    with open(f"{item.name}.hjson", "w") as file:
                        file.write(hjson)
            progress["value"] += 1
    os.chdir(file_path)
    
    if liquid_list:
        os.chdir("content")
        os.chdir("liquids")
        for liquid in liquid_list:
            for id in id_list:
                if liquid.name == id['name']:
                    hjson = create_hjson_liquid_file(liquid)
                    shutil.copy(id['image_path'],  os.path.join(file_path, "sprites/items/liquids"))
                    with open(f"{liquid.name}.hjson", "w") as file:
                        file.write(hjson)
            progress["value"] += 1
    os.chdir(file_path)
    
    print("Mod created successfully!")
    
    progress.destroy()


# creation of fhe mod structure for export
def create_folder(file_path):
    """
    Creates a directory structure for a project at the specified file path.
    The structure includes the following folders:
    ├── bundles
    ├── campaign
    ├── content
    │   ├── blocks
    │   │   ├── distribution
    │   │   ├── drills
    │   │   ├── effect
    │   │   ├── environment
    │   │   ├── liquids
    │   │   ├── logic
    │   │   ├── power
    │   │   ├── production
    │   │   ├── storage
    │   │   ├── turrets
    │   │   ├── units
    │   │   ├── walls
    │   ├── items
    │   ├── liquids
    │   ├── planets
    │   ├── sectors
    │   ├── status
    │   ├── units
    │   ├── weathers
    │   ├── maps
    │   ├── schematics
    │   ├── scripts
    │   ├── sounds
    ├── sprites
    │   ├── blocks
    │   │   ├── distribution
    │   │   ├── drills
    │   │   ├── effect
    │   │   ├── environment
    │   │   ├── liquids
    │   │   ├── logic
    │   │   ├── power
    │   │   ├── production
    │   │   ├── storage
    │   │  ├── turrets
    │   │   ├── units
    │   │   ├── walls
    │   ├── items
    │   │   ├── liquids
    │   ├── shapes
    │   ├── status
    │   ├── units
    Args:
        file_path (str): The path where the directory structure will be created.
    """
    os.chdir(file_path)
    os.mkdir("bundles")
    os.mkdir("campaign")
    # Content folder
    os.mkdir("content")
    os.chdir("content")
    os.mkdir("blocks")
    os.chdir("blocks")
    os.mkdir("distribution")
    os.mkdir("drills")
    os.mkdir("effect")
    os.mkdir("environment")
    os.mkdir("liquids")
    os.mkdir("logic")
    os.mkdir("power")
    os.mkdir("production")
    os.mkdir("storage")
    os.mkdir("turrets")
    os.mkdir("units")
    os.mkdir("walls")
    os.chdir("..")

    os.mkdir("items")
    os.mkdir("liquids")
    os.mkdir("planets")
    os.mkdir("sectors")
    os.mkdir("status")
    os.mkdir("units")
    os.mkdir("weathers")
    os.chdir("..")
    os.mkdir("maps")
    os.mkdir("schematics")
    os.mkdir("scripts")
    os.mkdir("sounds")

    # Sprites folder
    os.mkdir("sprites")
    os.chdir("sprites")
    os.mkdir("blocks")
    os.chdir("blocks")
    os.mkdir("distribution")
    os.mkdir("drills")
    os.mkdir("effect")
    os.mkdir("environment")
    os.mkdir("liquids")
    os.mkdir("logic")
    os.mkdir("power")
    os.mkdir("production")
    os.mkdir("storage")
    os.mkdir("turrets")
    os.mkdir("units")
    os.mkdir("walls")
    os.chdir("..")

    os.mkdir("items")
    os.chdir("items")
    os.mkdir("liquids")
    os.chdir("..")

    os.mkdir("shapes")
    os.mkdir("status")
    os.mkdir("units")

