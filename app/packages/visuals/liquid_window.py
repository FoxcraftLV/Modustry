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

def liquid_creator(root: Tk)->None:
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
    except:
        user = os.getlogin()
        icon_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Modustry\\data\\icons\\main_icon.ico"
    window.iconbitmap(icon_path)
    
    picture_box = Label(window, image=picture)
    picture_box._strong_ref_image = picture
    picture_box.grid(row=0, column=2)
    
    window.lift()
    window.pack_propagate()