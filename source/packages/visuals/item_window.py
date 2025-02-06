# Screen modules
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from customtkinter import *


# Data modules
from ..data.variables import id_list
from .global_func import choose_color

# Mindustry class
from ..data.mindustry_class.unlockableContent import UnlockableContent
from ..data.mindustry_class.Item import Item

def limit_name_lenght(name):
    """
    Limits the length of the input string to a specified maximum length.

    Args:
        name (tkinter.StringVar): A Tkinter StringVar object containing the string to be limited.

    The function truncates the string to a maximum of 30 characters if it exceeds this length.
    """
    limit = 30
    value = name.get()
    if len(value) > limit:
        name.set(value[:limit])

def item_creator(root: Tk, callback) -> None:
    """
    Creates a new item using a graphical user interface (GUI) for input.
    This function opens a window where the user can input various properties for an item,
    such as name, color, explosiveness, flammability, radioactivity, charge, hardness, cost,
    health scaling, and other attributes. The user can also select an image for the item.
    Args:
        root (Tk): The root Tkinter window.
        callback (function): A callback function to be called with the created item and image path.
        hardness (tkinter.IntVar): The hardness value of the item.
        lowPriority (tkinter.StringVar): Whether the item has low priority.
        buildable (tkinter.StringVar): Whether the item is buildable.
        hidden (tkinter.StringVar): Whether the item is hidden.
        hiddenOnPlanets (list): A list of planets where the item is hidden.
        description (tkinter.StringVar): The description of the item.
        alwaysUnlocked (tkinter.StringVar): Whether the item is always unlocked.
        inlineDescription (tkinter.StringVar): Whether the item has an inline description.
        hideDetails (tkinter.StringVar): Whether to hide details of the item.
        generateIcons (tkinter.StringVar): Whether to generate icons for the item.
        iconId (tkinter.IntVar): The icon ID of the item.
        selectionSize (tkinter.DoubleVar): The selection size of the item.
        fullOverride (tkinter.StringVar): Whether the item has a full override.
        picture_path (str): The file path of the selected image.
        picture (ImageTk.PhotoImage): The loaded image for the item.
    Methods:
        on_save(): Handles the save action for creating an item. Creates an `Item` object with
                   the provided attributes and calls the callback function with the created item
                   and image path.
    """
    
    ##### Variables #####
    item_created = False


    dark_color_1 = "#1A1A1A"
    gray_color_1 = "#6a6a6a"
    light_blue_color = "#408ef2"
    hover_color = "#1f4676"
    dark_blue_color = "#2c63aa"
    whiteColor= '#eeeeee'
    
    #TODO: Optimize var gestion
    name = StringVar()
    color = StringVar(value="#000000")
    explosiveness = DoubleVar(value=0.0)
    flammability = DoubleVar(value=0.0)
    radioactivity = DoubleVar(value=0.0)
    charge = DoubleVar(value=0.0)
    hardness = IntVar(value=0)
    cost = DoubleVar(value=1)
    healthScaling = DoubleVar(value=1.0)
    lowPriority = StringVar(value="false")
    frames = IntVar(value=0)
    transitionFrames = IntVar(value=0)
    frameTime = DoubleVar(value=5.0)
    buildable = StringVar(value="true")
    hidden = StringVar(value="false")
    hiddenOnPlanets = []
    
    # Global variables
    localizedName = StringVar()
    description = StringVar(value="Just a little description")
    details = StringVar()
    alwaysUnlocked = StringVar(value="false")
    inlineDescription = StringVar(value="true") 
    hideDetails = StringVar(value="true")
    generateIcons = StringVar(value="true")
    iconId = IntVar(value=0)
    selectionSize = DoubleVar(value=24.0)
    # uiIcon
    # fullIcon
    fullOverride = StringVar()
    # Image loader
    picture_path = filedialog.askopenfilename(title="Select your sprite (48x48 recommended)", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    picture = ImageTk.PhotoImage(Image.open(picture_path).resize((256, 256), Image.NEAREST))
    name.trace('w', lambda *args: limit_name_lenght(name))
    name.set(os.path.basename(picture_path).split(".")[0])
    
    # Window
    window = CTkToplevel(root)
    window.title("Item Creator")
    window.resizable(False, False)

    window.geometry(f"+500+10")
    window.attributes('-topmost', True)


    # icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "icons", "main_ico.ico")
    # icon_path = os.path.normpath(icon_path)
    
    try:
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
        icon_path = os.path.join(parent_dir, "icons\\main_ico.ico")
        if not os.path.isfile(icon_path):
            raise FileNotFoundError("Le fichier à l'emplacement {icon_path} n'existe pas.")
    except Exception:
        user = os.getlogin()
        icon_path = f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Modustry\\icons\\main_ico.ico"
    window.after(250, lambda: window.iconbitmap(icon_path))
    
    # Label frames
    UC_box = LabelFrame(window, text="Global Properties", bg=dark_color_1,fg = whiteColor,font=CTkFont(size = 28))
    UC_box.grid(row=0, column=0, padx=10,pady=10)
    
    item_box = LabelFrame(window, text="Item properties", bg=dark_color_1,fg = whiteColor,font=CTkFont(size = 28))
    item_box.grid(row=0, column=1, padx=10,pady=10)
    
    picture_box = Label(window, image=picture)
    picture_box._strong_ref_image = picture
    picture_box.grid(row=0, column=2, padx=10,pady=10)
    
    ##### Unlockable Content parameters #####
    name_box = LabelFrame(UC_box,bg = dark_color_1,font=CTkFont(size = 16))
    name_box.pack(side=TOP, pady=10, padx=5)
    name_Label = Label(name_box, text="Identification Name: ",bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18))
    name_Entry = Entry(name_box, textvariable=name,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),insertbackground=whiteColor)
    name_Label.pack(side=LEFT, pady=5)
    name_Entry.pack(side=LEFT, padx=5)
    
    description_box = LabelFrame(UC_box,bg = dark_color_1)
    description_box.pack(side=TOP)
    description_Label = Label(description_box, text="Main description: ",bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18))
    description_Text = Text(description_box, height=5, width=20,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),insertbackground=whiteColor)
    description_Label.pack(side=LEFT)
    description_Text.pack(side=LEFT, pady=5, padx=5)
    #description_Scrollbar = Scrollbar(description_box, orient=VERTICAL, command=description_Text.yview,bg = dark_color_1)
    #description_Scrollbar.pack(side=LEFT)
    
    localizedName_box = LabelFrame(UC_box,bg = dark_color_1)
    localizedName_box.pack(side=TOP, pady=10, padx=5)
    localizedName_Label = Label(localizedName_box, text="Name in-game",bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18))
    localizedName_Entry = Entry(localizedName_box, textvariable=localizedName,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),insertbackground=whiteColor)
    localizedName_Label.pack(side=LEFT)
    localizedName_Entry.pack(side=LEFT, padx=5, pady=5)
    
    alwaysUnlocked_Check = CTkCheckBox(UC_box, text="Unlocked in tech tree", variable=alwaysUnlocked, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    alwaysUnlocked_Check.pack(side=TOP,padx=50, anchor="w")
    
    inlineDescription_Check = CTkCheckBox(UC_box, text="Description in Tech Tree", variable=inlineDescription, fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    inlineDescription_Check.pack(side=TOP,padx=50, anchor="w")
    
    hideDetails_Check = CTkCheckBox(UC_box, text="Hide details in custom games", variable=hideDetails, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    hideDetails_Check.pack(side=TOP,padx=50, anchor="w")
    
    generateIcons_Check = CTkCheckBox(UC_box, text="Have an icon", variable=generateIcons, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    generateIcons_Check.pack(side=TOP,padx=50, anchor="w")
    

    selectionSize_Scale = Scale(UC_box, label="Size of the content (%)", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=selectionSize,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    selectionSize_Scale.pack(side=TOP, pady=10)
    
    
    
    ### Item parameters #####
    color_Button = CTkButton(item_box, text="Choose the color", command=lambda: color.set((choose_color(window, color_Button))),
                            height=30, fg_color=light_blue_color,hover_color=dark_blue_color,text_color=dark_color_1,
                            font=CTkFont(size = 18))
    color_Button.pack(side=TOP, pady=10)
    
    scale_box = LabelFrame(item_box, bg = dark_color_1)
    scale_box.pack(side=TOP, padx=10)
    
    explosiveness_Scale = Scale(scale_box, label="Explosiveness", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=explosiveness,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    explosiveness_Scale.grid(row=0, column=0, padx=(10,5),pady=(10,5))
    
    flammability_Scale = Scale(scale_box, label="Flammability", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=flammability,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    flammability_Scale.grid(row=0, column=1, padx=(5,10),pady=(10,5))
    
    radioactivity_Scale = Scale(scale_box, label="Radioactivity", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=radioactivity,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    radioactivity_Scale.grid(row=1, column=0, padx=(10,5),pady=5)
    
    charge_Scale = Scale(scale_box, label="Charge", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=charge,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    charge_Scale.grid(row=1, column=1, padx=(5,10),pady=5)
    
    hardness_Scale = Scale(scale_box, label="Hardness", from_=0, to=10, tickinterval=5, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=hardness,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    hardness_Scale.grid(row=2, column=0, padx=(10,5),pady=5)
    
    cost_Scale = Scale(scale_box, label="Cost", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=cost,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    cost_Scale.grid(row=2, column=1, padx=(5,10),pady=5)
    
    healthScaling_Scale = Scale(scale_box, label="Health Scaling", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=healthScaling,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    healthScaling_Scale.grid(row=3, column=0, padx=(10,5),pady=5)
    
    frames_Scale = Scale(scale_box, label="Frames", from_=0, to=60, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=frames,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    frames_Scale.grid(row=3, column=1, padx=(5,10),pady=5)
    
    transitionFrames_Scale = Scale(scale_box, label="Transition frames", from_=0, to=60, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=transitionFrames,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    transitionFrames_Scale.grid(row=4, column=0, padx=(10,5),pady=(5,10))
    
    frameTime_Scale = Scale(scale_box, label="Frame time", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=frameTime,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    frameTime_Scale.grid(row=4, column=1, padx=(5,10),pady=(5,10))
    
    #TODO: hiddenOnPlanets
    
    check_box = LabelFrame(item_box,bg = dark_color_1)
    check_box.pack(side=TOP, pady=10)
    lowPriority_Check = CTkCheckBox(check_box, text="Low Priority", variable=lowPriority, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    lowPriority_Check.grid(row=0, column=0, padx=5, sticky="w")
    buildable_Check = CTkCheckBox(check_box, text="Is buildable", variable=buildable, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    buildable_Check.grid(row=0, column=1, padx=5, sticky="w")
    hidden_Check = CTkCheckBox(check_box, text="Is hidden", variable=hidden, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    hidden_Check.grid(row=1, column=0, padx=5, sticky="w")
    
    def on_save():
        """
        Handles the save action for creating an item.

        This function creates an `Item` object with various attributes obtained from
        the user input fields if the item has not been created yet. It then sets the
        `item_created` flag to True, stores the image path, destroys the window, and
        calls the provided callback function with the created item and image path.

        Attributes:
            item_created (bool): A flag indicating whether the item has been created.
            name (tkinter.StringVar): The name of the item.
            color (tkinter.StringVar): The color of the item in hexadecimal format.
            explosiveness (tkinter.DoubleVar): The explosiveness value of the item.
            flammability (tkinter.DoubleVar): The flammability value of the item.
            radioactivity (tkinter.DoubleVar): The radioactivity value of the item.
            charge (tkinter.DoubleVar): The charge value of the item.
            hardness (tkinter.DoubleVar): The hardness value of the item.
            cost (tkinter.DoubleVar): The cost value of the item.
            healthScaling (tkinter.DoubleVar): The health scaling value of the item.
            lowPriority (tkinter.BooleanVar): Whether the item has low priority.
            frames (tkinter.IntVar): The number of frames for the item.
            transitionFrames (tkinter.IntVar): The number of transition frames for the item.
            frameTime (tkinter.DoubleVar): The frame time for the item.
            buildable (tkinter.BooleanVar): Whether the item is buildable.
            hidden (tkinter.BooleanVar): Whether the item is hidden.
            hiddenOnPlanets (bool): Whether the item is hidden on planets.
            localizedName (tkinter.StringVar): The localized name of the item.
            description_Text (tkinter.Text): The description text of the item.
            details (tkinter.StringVar): The details of the item.
            alwaysUnlocked (tkinter.BooleanVar): Whether the item is always unlocked.
            inlineDescription (tkinter.BooleanVar): Whether the item has an inline description.
            hideDetails (tkinter.BooleanVar): Whether to hide details of the item.
            generateIcons (tkinter.BooleanVar): Whether to generate icons for the item.
            iconId (tkinter.StringVar): The icon ID of the item.
            selectionSize (tkinter.IntVar): The selection size of the item.
            fullOverride (tkinter.BooleanVar): Whether the item has a full override.

        Parameters:
            None

        Returns:
            None
        """
        nonlocal item_created
        if not item_created:
            item = Item(
                        name=name.get(),
                        color=color.get()[1:],
                        explosiveness=explosiveness.get(),
                        flammability=flammability.get(),
                        radioactivity=radioactivity.get(),
                        charge=charge.get(),
                        hardness=hardness.get(),
                        cost=cost.get(),
                        healthScaling=healthScaling.get(),
                        lowPriority=lowPriority.get(),
                        frames=frames.get(),
                        transitionFrames=transitionFrames.get(),
                        frameTime=frameTime.get(),
                        buildable=buildable.get(),
                        hidden=hidden.get(),
                        hiddenOnPlanets=hiddenOnPlanets,
                        localizedName=localizedName.get(),
                        description=description_Text.get(index1='1.0', index2=END).strip(),
                        details=details.get(),
                        alwaysUnlocked=alwaysUnlocked.get(),
                        inlineDescription=inlineDescription.get(),
                        hideDetails=hideDetails.get(),
                        generateIcons=generateIcons.get(),
                        iconId=iconId.get(),
                        selectionSize=selectionSize.get(),
                        fullOverride=fullOverride.get()
                )
            image_path = picture_path
            item_created = True
            # TODO: Make a better way to store id_list
            window.destroy()
            callback(item, image_path)
    
    saveButton = CTkButton(window, text="Save", command=on_save, width = 100, height=40, fg_color=light_blue_color,
                            hover_color=dark_blue_color,text_color=dark_color_1, font=CTkFont(size = 24))
    saveButton.grid(row=1, column=0, pady=(0, 20))

    
    # Show the window
    window.lift()
    window.pack_propagate()

def create_hjson_item_file(item: Item):
    """
    Creates an HJSON representation of an item.
    Args:
        item (Item): The item object containing various attributes.
    Returns:
        str: A string containing the HJSON representation of the item.
    """
    if item.fullOverride == "":
        item.fullOverride = "true"

    hjson = f"""
    {{
        type: Item,
        name: '{item.name}',
        localizedName: '{item.localizedName}',
        description: '{item.description}',
        detail: '{item.details}',
        alwaysUnlocked: {item.alwaysUnlocked},
        inlineDescription: {item.inlineDescription},
        hideDetails: {item.hideDetails},
        generateIcons: {item.generateIcons},
        iconId: {item.iconId},
        selectionSize: {item.selectionSize},
        fullOverride: {item.fullOverride},
        color: '{item.color}',
        explosiveness: {item.explosiveness},
        flammability: {item.flammability},
        radioactivity: {item.radioactivity},
        charge: {item.charge},
        hardness: {item.hardness},
        cost: {item.cost},
        healthScaling: {item.healthScaling},
        lowPriority: {item.lowPriority},
        frames: {item.frames},
        transitionFrames: {item.transitionFrames},
        frameTime: {item.frameTime},
        buildable: {item.buildable},
        hidden: {item.hidden},
        hiddenOnPlanets: {item.hiddenOnPlanets}
    }}
    """
    return hjson
