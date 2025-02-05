# Screen modules
from tkinter import *
from tkinter import filedialog
from tokenize import String
from PIL import ImageTk, Image
import os
from customtkinter import *


# Data modules
from ..data.variables import id_list
from .global_func import choose_color

# Mindustry class
from ..data.mindustry_class.unlockableContent import UnlockableContent
from ..data.mindustry_class.Liquid import Liquid

def limit_name_lenght(name):
    """
    Trims the input string to a maximum length of 30 characters.

    Parameters:
    name (tkinter.StringVar): A Tkinter StringVar object containing the string to be trimmed.

    Returns:
    None
    """
    limit = 30
    value = name.get()
    if len(value) > limit:
        name.set(value[:limit])


def liquid_creator(root: Tk, callback) -> None:
    """
    Creates a GUI window for configuring and creating a liquid object with various properties.
    Args:
        root (Tk): The root Tkinter window.
        callback (function): A callback function to be called with the created liquid object and image path.
    Variables:
        liquid_created (bool): Flag to check if the liquid has been created.
        dark_color_1 (str): Dark color for UI elements.
        gray_color_1 (str): Gray color for UI elements.
        light_blue_color (str): Light blue color for UI elements.
        hover_color (str): Hover color for UI elements.
        dark_blue_color (str): Dark blue color for UI elements.
        whiteColor (str): White color for UI elements.
        name (StringVar): Variable to store the name of the liquid.
        color (StringVar): Variable to store the color of the liquid.
        gasColor (StringVar): Variable to store the gas color of the liquid.
        barColor (StringVar): Variable to store the bar color of the liquid.
        lightColor (StringVar): Variable to store the light color of the liquid.
        flammability (DoubleVar): Variable to store the flammability of the liquid.
        explosiveness (DoubleVar): Variable to store the explosiveness of the liquid.
        hidden (StringVar): Variable to store if the liquid is hidden.
        canStayOn (list): List to store the blocks the liquid can stay on.
        blockReactive (StringVar): Variable to store if the liquid is block reactive.
        coolant (StringVar): Variable to store if the liquid is a coolant.
        moveThroughBlocks (StringVar): Variable to store if the liquid can move through blocks.
        incinerate (StringVar): Variable to store if the liquid can incinerate.
        effect (StringVar): Variable to store the effect of the liquid.
        particleEffect (StringVar): Variable to store the particle effect of the liquid.
        particleSpacing (DoubleVar): Variable to store the particle spacing of the liquid.
        boilPoint (DoubleVar): Variable to store the boil point of the liquid.
        capPuddles (StringVar): Variable to store if the liquid can cap puddles.
        vaporEffect (StringVar): Variable to store the vapor effect of the liquid.
        temperature (DoubleVar): Variable to store the temperature of the liquid.
        heatCapacity (DoubleVar): Variable to store the heat capacity of the liquid.
        viscosity (DoubleVar): Variable to store the viscosity of the liquid.
        animationFrames (IntVar): Variable to store the animation frames of the liquid.
        animationScaleGas (DoubleVar): Variable to store the animation scale for gas of the liquid.
        animationScaleLiquid (DoubleVar): Variable to store the animation scale for liquid of the liquid.
        gas (StringVar): Variable to store if the liquid is a gas.
        localizedName (StringVar): Variable to store the localized name of the liquid.
        description (StringVar): Variable to store the description of the liquid.
        details (StringVar): Variable to store the details of the liquid.
        alwaysUnlocked (StringVar): Variable to store if the liquid is always unlocked.
        inlineDescription (StringVar): Variable to store if the liquid has an inline description.
        hideDetails (StringVar): Variable to store if the details of the liquid are hidden.
        generateIcons (StringVar): Variable to store if the liquid generates icons.
        iconId (IntVar): Variable to store the icon ID of the liquid.
        selectionSize (DoubleVar): Variable to store the selection size of the liquid.
        fullOverride (StringVar): Variable to store the full override of the liquid.
        picture_path (str): Path to the picture of the liquid.
        picture (ImageTk.PhotoImage): Image of the liquid.
        window (CTkToplevel): The main window for the liquid creator.
        UC_box (LabelFrame): Label frame for global properties.
        liquid_box (LabelFrame): Label frame for liquid properties.
        picture_box (Label): Label to display the picture of the liquid.
        name_box (LabelFrame): Label frame for the name input.
        name_Label (Label): Label for the name input.
        name_Entry (Entry): Entry for the name input.
        description_box (LabelFrame): Label frame for the description input.
        description_Label (Label): Label for the description input.
        description_Text (Text): Text widget for the description input.
        localizedName_box (LabelFrame): Label frame for the localized name input.
        localizedName_Label (Label): Label for the localized name input.
        localizedName_Entry (Entry): Entry for the localized name input.
        alwaysUnlocked_Check (CTkCheckBox): Checkbox for always unlocked option.
        inlineDescription_Check (CTkCheckBox): Checkbox for inline description option.
        hideDetails_Check (CTkCheckBox): Checkbox for hide details option.
        generateIcons_Check (CTkCheckBox): Checkbox for generate icons option.
        selectionSize_Scale (Scale): Scale for selection size.
        button_Frame (LabelFrame): Frame for color buttons.
        color_Button (CTkButton): Button to choose the color.
        gasColor_Button (CTkButton): Button to choose the gas color.
        barColor_Button (CTkButton): Button to choose the bar color.
        lightColor_Button (CTkButton): Button to choose the light color.
        scale_box (LabelFrame): Frame for scales.
        flammability_Scale (Scale): Scale for flammability.
        temperature_Scale (Scale): Scale for temperature.
        heatCapacity_Scale (Scale): Scale for heat capacity.
        viscosity_Scale (Scale): Scale for viscosity.
        explosiveness_Scale (Scale): Scale for explosiveness.
        particleSpacing_Scale (Scale): Scale for particle spacing.
        boilPoint_Scale (Scale): Scale for boil point.
        animationFrames_Scale (Scale): Scale for animation frames.
        animationScaleGas_Scale (Scale): Scale for animation scale gas.
        animationScaleLiquid_Scale (Scale): Scale for animation scale liquid.
        check_box (LabelFrame): Frame for checkboxes.
        hidden_Check (CTkCheckBox): Checkbox for hidden option.
        blockReactive_Check (CTkCheckBox): Checkbox for block reactive option.
        coolant_Check (CTkCheckBox): Checkbox for coolant option.
        moveThroughBlocks_Check (CTkCheckBox): Checkbox for move through blocks option.
        incinerate_Check (CTkCheckBox): Checkbox for incinerate option.
        capPuddles_Check (CTkCheckBox): Checkbox for cap puddles option.
        gas_Check (CTkCheckBox): Checkbox for gas option.
        saveButton (CTkButton): Button to save the liquid.
    Functions:
        on_save(): Callback function to save the liquid object and call the provided callback with the liquid and image path.
    """
    ##### Variables #####
    liquid_created = False


    dark_color_1 = "#1A1A1A"
    gray_color_1 = "#6a6a6a"
    light_blue_color = "#408ef2"
    hover_color = "#1f4676"
    dark_blue_color = "#2c63aa"
    whiteColor= '#eeeeee'

    
    #TODO: Optimize var gestion
    name = StringVar()
    color = StringVar(value="#000000")
    gasColor = StringVar(value="#000000")
    barColor = StringVar(value="#000000")
    lightColor = StringVar(value="#000000")
    flammability = DoubleVar(value=0.0)
    explosiveness = DoubleVar(value=0.0)
    hidden = StringVar(value="false")
    canStayOn = []
    blockReactive = StringVar(value="true")
    coolant = StringVar(value="true")
    moveThroughBlocks = StringVar(value="false")
    incinerate = StringVar(value="true")
    effect = StringVar(value="none")
    particleEffect = StringVar(value="none")
    particleSpacing = DoubleVar(value=60.0)
    boilPoint = DoubleVar(value=2.0)
    capPuddles = StringVar(value="true")
    vaporEffect = StringVar(value="vapor")
    temperature = DoubleVar(value=0.5)
    heatCapacity = DoubleVar(value=0.5)
    viscosity = DoubleVar(value=0.5)
    animationFrames = IntVar(value=50)
    animationScaleGas = DoubleVar(value=190.0)
    animationScaleLiquid = DoubleVar(value=230.0)
    gas = StringVar(value="false")
    
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
    window.title("Liquid Creator")
    window.resizable(False, False)

    window.geometry(f"+150+10")
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
        icon_path = f"C:\\Users\\{user}\\AppData\\Local\\Programs\\Modustry\\main_icon.ico"
    window.after(250, lambda: window.iconbitmap(icon_path))
    
    # Label frames
    UC_box = LabelFrame(window, text="Global Properties", bg=dark_color_1,fg = whiteColor,font=CTkFont(size = 28))
    UC_box.grid(row=0, column=0, padx=10,pady=10)
    
    liquid_box = LabelFrame(window, text="Liquid Properties", bg=dark_color_1,fg = whiteColor,font=CTkFont(size = 28))
    liquid_box.grid(row=0, column=1, padx=10,pady=10)
    
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
    
    
    ### Liquid parameters #####
    button_Frame = LabelFrame(liquid_box,bg = dark_color_1)
    button_Frame.grid(row=0, column=0, padx=10,pady=5)
    
    color_Button = CTkButton(button_Frame, text="Choose the color", command=lambda: color.set((choose_color(window, color_Button))),
                            width=200, height=30, fg_color=light_blue_color,hover_color=dark_blue_color,text_color=dark_color_1,
                            font=CTkFont(size = 18))
    color_Button.grid(row=0, column=0, pady=5, padx=5)
    
    gasColor_Button = CTkButton(button_Frame, text="Choose the gas color", command=lambda: gasColor.set((choose_color(window, gasColor_Button))),
                            width=200, height=30, fg_color=light_blue_color,hover_color=dark_blue_color,text_color=dark_color_1,
                            font=CTkFont(size = 18))
    gasColor_Button.grid(row=0, column=1, pady=5, padx=(0,5))
    
    barColor_Button = CTkButton(button_Frame, text="Choose the bar color", command=lambda: barColor.set((choose_color(window, barColor_Button))),
                            width=200, height=30, fg_color=light_blue_color,hover_color=dark_blue_color,text_color=dark_color_1,
                            font=CTkFont(size = 18))
    barColor_Button.grid(row=1, column=0, pady=(0,5), padx=5)
    
    lightColor_Button = CTkButton(button_Frame, text="Choose the light color", command=lambda: lightColor.set((choose_color(window, lightColor_Button))),
                            width=200, height=30, fg_color=light_blue_color,hover_color=dark_blue_color,text_color=dark_color_1,
                            font=CTkFont(size = 18))
    lightColor_Button.grid(row=1, column=1, pady=(0,5), padx=(0,5))
    
    scale_box = LabelFrame(liquid_box, bg = dark_color_1)
    scale_box.grid(row=1, column=0, padx=10,pady=20)
    
    flammability_Scale = Scale(scale_box, label="Flammability", from_=0, to=1, tickinterval=0.5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=flammability,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    flammability_Scale.grid(row=0, column=0, padx=(10,5),pady=(10,5))
    
    temperature_Scale = Scale(scale_box, label="Temperature", from_=0, to=1, tickinterval=0.5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=temperature,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    temperature_Scale.grid(row=2, column=0, padx=(10,5),pady=5)
    
    heatCapacity_Scale = Scale(scale_box, label="Heat capacity", from_=0, to=1, tickinterval=0.5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=heatCapacity,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    heatCapacity_Scale.grid(row=2, column=1, padx=(5,10),pady=5)
    
    viscosity_Scale = Scale(scale_box, label="Viscosity", from_=0, to=1, tickinterval=0.5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=viscosity,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    viscosity_Scale.grid(row=3, column=0, padx=(10,5),pady=5)
    
    explosiveness_Scale = Scale(scale_box, label="Explosiveness", from_=0, to=1, tickinterval=0.5, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=explosiveness,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    explosiveness_Scale.grid(row=0, column=1, padx=(5,10),pady=(10,5))
    
    particleSpacing_Scale = Scale(scale_box, label="Particle spacing", from_=0, to=100, tickinterval=25, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=particleSpacing,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    particleSpacing_Scale.grid(row=1, column=0, padx=(10,5),pady=5)
    
    boilPoint_Scale = Scale(scale_box, label="Boil point", from_=0, to=100, tickinterval=25, resolution=0.1, orient=HORIZONTAL, sliderlength=30, variable=boilPoint,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    boilPoint_Scale.grid(row=1, column=1, padx=(5,10),pady=5)
    
    animationFrames_Scale = Scale(scale_box, label="Animation frames", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=animationFrames,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    animationFrames_Scale.grid(row=3, column=1, padx=(5,10),pady=5)
    
    animationScaleGas_Scale = Scale(scale_box, label="Animation scale gas", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=animationScaleGas,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    animationScaleGas_Scale.grid(row=4, column=0, padx=(10,5),pady=(5,10))
    
    animationScaleLiquid_Scale = Scale(scale_box, label="Animation scale liquid", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=animationScaleLiquid,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    animationScaleLiquid_Scale.grid(row=4, column=1, padx=(5,10),pady=(5,10))
    
    
    #TODO: hiddenOnPlanets
    
    check_box = LabelFrame(liquid_box,bg = dark_color_1)
    check_box.grid(row=0, column=1, padx=10,pady=5)
    
    hidden_Check = CTkCheckBox(check_box, text="Hidden", variable=hidden, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    hidden_Check.pack(side=TOP,padx=10, anchor="w")
    
    blockReactive_Check = CTkCheckBox(check_box, text="Block reactive", variable=blockReactive, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    blockReactive_Check.pack(side=TOP,padx=10, anchor="w")
    
    coolant_Check = CTkCheckBox(check_box, text="Coolant", variable=coolant, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    coolant_Check.pack(side=TOP,padx=10, anchor="w")
    
    moveThroughBlocks_Check = CTkCheckBox(check_box, text="Move through blocks", variable=moveThroughBlocks, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    moveThroughBlocks_Check.pack(side=TOP,padx=10, anchor="w")
    
    incinerate_Check = CTkCheckBox(check_box, text="Incinerate", variable=incinerate, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    incinerate_Check.pack(side=TOP,padx=10, anchor="w")
    
    capPuddles_Check = CTkCheckBox(check_box, text="Cap puddles", variable=capPuddles, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    capPuddles_Check.pack(side=TOP,padx=10, anchor="w")
    
    gas_Check = CTkCheckBox(check_box, text="Gas", variable=gas, offvalue="false", onvalue="true", fg_color= dark_blue_color,bg_color = dark_color_1,text_color = whiteColor,font=CTkFont(size = 14), checkbox_height=15, checkbox_width=15, checkmark_color=whiteColor,border_width= 2, corner_radius=5, border_color=whiteColor, hover_color=hover_color)
    gas_Check.pack(side=TOP,padx=10, anchor="w")
    
    def on_save():
        """
        Handles the save action for creating a new Liquid object with the provided attributes.
        
        This function checks if a liquid has already been created. If not, it creates a new Liquid 
        object using the values from various input fields, sets the image path, marks the liquid 
        as created, destroys the window, and calls the callback function with the new liquid and 
        image path.

        Attributes:
            liquid_created (bool): A flag indicating whether the liquid has already been created.
            name (tk.StringVar): The name of the liquid.
            localizedName (tk.StringVar): The localized name of the liquid.
            description (tk.StringVar): The description of the liquid.
            details (tk.StringVar): Additional details about the liquid.
            alwaysUnlocked (tk.BooleanVar): Whether the liquid is always unlocked.
            inlineDescription (tk.BooleanVar): Whether the liquid has an inline description.
            hideDetails (tk.BooleanVar): Whether to hide details of the liquid.
            generateIcons (tk.BooleanVar): Whether to generate icons for the liquid.
            iconId (tk.StringVar): The icon ID for the liquid.
            selectionSize (tk.IntVar): The selection size for the liquid.
            fullOverride (tk.BooleanVar): Whether to fully override existing properties.
            picture_path (str): The file path to the liquid's picture.
            color (tk.StringVar): The color of the liquid.
            gasColor (tk.StringVar): The color of the gas form of the liquid.
            barColor (tk.StringVar): The color of the liquid's bar representation.
            lightColor (tk.StringVar): The color of the liquid's light representation.
            flammability (tk.DoubleVar): The flammability of the liquid.
            explosiveness (tk.DoubleVar): The explosiveness of the liquid.
            hidden (tk.BooleanVar): Whether the liquid is hidden.
            canStayOn (bool): Whether the liquid can stay on blocks.
            blockReactive (tk.BooleanVar): Whether the liquid is reactive with blocks.
            coolant (tk.BooleanVar): Whether the liquid can be used as a coolant.
            moveThroughBlocks (tk.BooleanVar): Whether the liquid can move through blocks.
            incinerate (tk.BooleanVar): Whether the liquid can incinerate.
            effect (tk.StringVar): The effect of the liquid.
            particleEffect (tk.StringVar): The particle effect of the liquid.
            particleSpacing (tk.DoubleVar): The spacing of particles in the liquid.
            boilPoint (tk.DoubleVar): The boiling point of the liquid.
            capPuddles (tk.BooleanVar): Whether to cap puddles of the liquid.
            vaporEffect (tk.StringVar): The vapor effect of the liquid.
            temperature (tk.DoubleVar): The temperature of the liquid.
            heatCapacity (tk.DoubleVar): The heat capacity of the liquid.
            viscosity (tk.DoubleVar): The viscosity of the liquid.
            animationFrames (tk.IntVar): The number of animation frames for the liquid.
            animationScaleGas (tk.DoubleVar): The animation scale for the gas form of the liquid.
            animationScaleLiquid (tk.DoubleVar): The animation scale for the liquid form.
            gas (tk.BooleanVar): Whether the liquid is in gas form.

        Returns:
            None
        """
        nonlocal liquid_created
        if not liquid_created:
            liquid = Liquid(
                name.get(),
                localizedName.get(),
                description.get(),
                details.get(),
                alwaysUnlocked.get(),
                inlineDescription.get(),
                hideDetails.get(),
                generateIcons.get(),
                iconId.get(),
                selectionSize.get(),
                fullOverride.get(),
                picture_path,
                color.get(),
                gasColor.get(),
                barColor.get(),
                lightColor.get(),
                flammability.get(),
                explosiveness.get(),
                hidden.get(),
                canStayOn,
                blockReactive.get(),
                coolant.get(),
                moveThroughBlocks.get(),
                incinerate.get(),
                effect.get(),
                particleEffect.get(),
                particleSpacing.get(),
                boilPoint.get(),
                capPuddles.get(),
                vaporEffect.get(),
                temperature.get(),
                heatCapacity.get(),
                viscosity.get(),
                animationFrames.get(),
                animationScaleGas.get(),
                animationScaleLiquid.get(),
                gas.get()
            )
            image_path = picture_path
            liquid_created = True
            # TODO: Make a better way to store id_list
            window.destroy()
            callback(liquid, image_path)
    
    saveButton = CTkButton(window, text="Save", command=on_save, width = 100, height=40, fg_color=light_blue_color,
                            hover_color=dark_blue_color,text_color=dark_color_1, font=CTkFont(size = 24))
    saveButton.grid(row=1, column=0, pady=(0, 20))

    
    # Show the window
    window.lift()
    window.pack_propagate()

def create_hjson_liquid_file(liquid: Liquid):
    """
    Generates an HJSON representation of a Liquid object.
    Args:
        liquid (Liquid): The Liquid object containing various properties.
    Returns:
        str: A string containing the HJSON representation of the Liquid object.
    """
    if liquid.fullOverride == "":
        liquid.fullOverride = "true"

    hjson = f"""
    {{
        type: liquid,
        name: '{liquid.name}',
        localizedName: '{liquid.localizedName}',
        description: '{liquid.description}',
        detail: '{liquid.details}',
        alwaysUnlocked: {liquid.alwaysUnlocked},
        inlineDescription: {liquid.inlineDescription},
        hideDetails: {liquid.hideDetails},
        generateIcons: {liquid.generateIcons},
        iconId: {liquid.iconId},
        selectionSize: {liquid.selectionSize},
        fullOverride: {liquid.fullOverride},
        color: {liquid.color[1:]},
        gasColor: {liquid.gasColor[1:]},
        barColor: {liquid.barColor[1:]},
        lightColor: {liquid.lightColor[1:]+"ff"},
        flammability: {liquid.flammability},
        explosiveness: {liquid.explosiveness},
        hidden: {liquid.hidden},
        canStayOn: {liquid.canStayOn},
        blockReactive: {liquid.blockReactive},
        coolant: {liquid.coolant},
        moveThroughBlocks: {liquid.moveThroughBlocks},
        incinerate: {liquid.incinerate},
        effect: {liquid.effect},
        particleEffect: {liquid.particleEffect},
        particleSpacing: {liquid.particleSpacing},
        boilPoint: {liquid.boilPoint},
        capPuddles: {liquid.capPuddles},
        vaporEffect: {liquid.vaporEffect},
        temperature: {liquid.temperature},
        heatCapacity: {liquid.heatCapacity},
        viscosity: {liquid.viscosity},
        animationFrames: {liquid.animationFrames},
        animationScaleGas: {liquid.animationScaleGas},
        animationScaleLiquid: {liquid.animationScaleLiquid},
        gas: {liquid.gas}
    }}
    """
    return hjson
