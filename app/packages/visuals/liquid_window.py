from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
# Data modules 
from ..data.variables import liquid_list, UC_list, id_list
from .global_func import choose_color

# Mindustry class
from ..data.mindustry_class.unlockableContent import UnlockableContent
from ..data.mindustry_class.Liquid import Liquid

def liquid_creator(root: Tk) -> None:
    ##### Variables #####
    #TODO: Optimize var gestion

    # Liquid variables
    name = StringVar()
    color = StringVar(value="#000000")
    gasColor = StringVar(value="#000000")
    barColor = StringVar(value="#000000")
    lightColor = StringVar(value="#00000000")
    flammability = DoubleVar(value=0.0)
    explosiveness = DoubleVar(value=0.0)
    hidden = StringVar(value="false")
    canStayOn = []
    blockReactive = StringVar(value="false")
    coolant = StringVar(value="true")
    moveThroughBlocks = StringVar(value="false")
    incinerate = StringVar(value="true")
    effect = StringVar(value="StatusEffects.none")
    particleEffect = StringVar(value="ParticleEffects.none")
    particleSpacing = DoubleVar(value=0.0)
    boilPoint = DoubleVar(value=0.0)
    capPuddles = StringVar(value="true")
    vaporEffect = StringVar(value="ParticleEffects.vapor")
    temperature = DoubleVar(value=0.0)
    heatCapacity = DoubleVar(value=0.0)
    viscosity = DoubleVar(value=0.0)
    animationFrames = IntVar(value=50)
    animationScaleGas = DoubleVar(value=0.0)
    animationScaleLiquid = DoubleVar(value=0.0)
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

    window = Toplevel(root)
    window.title('Liquid Creator')
    try:
        icon_path = os.path.join(os.path.dirname(__file__), "icons\\main_ico.ico")
        if not os.path.isfile(icon_path):
            raise FileNotFoundError("Le fichier à l'emplacement {icon_path} n'existe pas.")
    except Exception:
        user = os.getlogin()
        icon_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Modustry\\data\\icons\\main_icon.ico"
    window.iconbitmap(icon_path)

    #Label frames 
    UC_box = LabelFrame(window, text="Global Properties")
    UC_box.grid(row=0, column=0)
    
    liquid_box = LabelFrame(window, text="Item properties")
    liquid_box.grid(row=0, column=1)
    
    picture_box = Label(window, image=picture)
    picture_box._strong_ref_image = picture
    picture_box.grid(row=0, column=2)
    
    ##### Unlockable Content parameters #####
    name_box = LabelFrame(UC_box)
    name_box.pack(side=TOP)
    name_Label = Label(name_box, text='Name in-game :')
    name_Entry = Entry(name_box, textvariable=name)
    name_Label.pack(side=LEFT)
    name_Entry.pack(side=LEFT)
    
    description_box = LabelFrame(UC_box)
    description_box.pack(side=TOP)
    description_Label = Label(description_box, text='Description :')
    description_Text = Text(description_box, width=30, height=5, wrap=WORD)
    description_Label.pack(side=LEFT)
    description_Text.pack(side=LEFT)
    description_Scrollbar = Scrollbar(description_box, orient=VERTICAL, command=description_Text.yview)
    description_Scrollbar.pack(side=LEFT)
    
    localizedName_box = LabelFrame(UC_box)
    localizedName_box.pack(side=TOP)
    localizedName_Label = Label(localizedName_box, text='Name in-game :')
    localizedName_Entry = Entry(localizedName_box, textvariable=localizedName)
    localizedName_Label.pack(side=LEFT)
    localizedName_Entry.pack(side=LEFT)
    
    alwaysUnlocked_Check = Checkbutton(UC_box, text="Unlocked in tech tree", variable=alwaysUnlocked, offvalue="false", onvalue="true")
    alwaysUnlocked_Check.pack(side=TOP)

    inlineDescription_Check = Checkbutton(UC_box, text="Description in Tech Tree", variable=inlineDescription)
    inlineDescription_Check.pack(side=TOP)

    hideDetails_Check = Checkbutton(UC_box, text="Hide details in custom games", variable=hideDetails, offvalue="false", onvalue="true")
    hideDetails_Check.pack(side=TOP)

    generateIcons_Check = Checkbutton(UC_box, text="Have an icon", variable=generateIcons, offvalue="false", onvalue="true")
    generateIcons_Check.pack(side=TOP)

    selectionSize_Scale = Scale(UC_box, label="Size of the content (%)", from_=0, to=100, tickinterval=25, resolution=0.5, orient=HORIZONTAL, sliderlength=25, variable=selectionSize)
    selectionSize_Scale.pack(side=TOP)
    
    ##### Liquid parameters #####
    color_Button = Button(liquid_box, text="Choose the color for filters", command=lambda: color.set(choose_color(window, color_Button)))
    color_Button.pack(side=TOP)
    
    scale_box = LabelFrame(liquid_box)
    scale_box.pack(side=TOP)
    
    gasColor_Button = Button(liquid_box, text="Choose the gas color", command=lambda: gasColor.set(choose_color(window, gasColor_Button)))
    gasColor_Button.pack(side=TOP)
    
    barColor_Button = Button(liquid_box, text="Choose the color in pipes", command=lambda: barColor.set(choose_color(window, gasColor_Button)))
    barColor_Button.pack(side=TOP)
    
    lightColor_Button = Button(liquid_box, text="Choose the light color", command=lambda: lightColor.set(choose_color(window, lightColor_Button)))
    lightColor_Button.pack(side=TOP)
    
    flammability_Scale = Scale(scale_box, label="Flammability", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=flammability)
    flammability_Scale.grid(row=0, column=1)
    
    explosiveness_Scale = Scale(scale_box, label="Explosiveness", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=explosiveness)
    explosiveness_Scale.grid(row=0, column=0)


    check_box = LabelFrame(liquid_box)
    check_box.pack(side=TOP)
    hidden_Check = Checkbutton(check_box, text="Is hidden", variable=hidden, offvalue="false", onvalue="true")
    hidden_Check.grid(row=1, column=0)



    window.lift()
    window.pack_propagate()