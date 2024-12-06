from tkinter import *
from tkinter import filedialog
from pickle import *
import os
import shutil

from packages.visuals.item_window import create_hjson_item_file
from packages.data.variables import *

def mod_window(root):
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
    
    create_button = Button(window, text='Create the mod', command=lambda: pack_all(name.get(), displayName.get(), author.get(), description_Text.get('1.0', 'end-1c'), minGameVersion.get(), hidden.get()))
    
    create_button.pack(side='top', anchor='n')
    
    window.pack_propagate()

# TODO: Optimize file writing to reduce I/O operations and improve performance
# FIXME: Improve error handling for file operations
def pack_all(name, displayName, author, description, minGameVersion, hidden):
    global already_packed, item_list, id_list, UC_list
    if not already_packed:
        file_path = filedialog.askdirectory(title="Select directory to save items")
        create_folder(file_path)
        already_packed = True
    os.chdir(file_path)
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
    if item_list:
        os.chdir("content")
        os.chdir("items")
        for item in item_list:
            for id in id_list:
                if item.name == id['name']:
                    hjson = create_hjson_item_file(item, UC_list[id['UC_id']])
                    shutil.copy(id['image_path'],  os.path.join(file_path, "sprites/items"))
                    with open(item.name + ".hjson", "w") as file:
                        file.write(hjson)

        print("Items created successfully!")
    os.chdir(file_path)


# creation o fhe mod structure for export
def create_folder(file_path):
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

