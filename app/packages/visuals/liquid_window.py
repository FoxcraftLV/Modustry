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

def liquid_creator(root: Tk, callback) -> None:
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
    effect = StringVar(value="StatusEffects.none")
    particleEffect = StringVar(value="Fx.none")
    particleSpacing = DoubleVar(value=60.0)
    boilPoint = DoubleVar(value=2.0)
    capPuddles = StringVar(value="true")
    vaporEffect = StringVar(value="Fx.vapor")
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
    
    # Window
    window = CTkToplevel(root)
    window.title("Liquid Creator")
    window.resizable(False, False)

    window.geometry(f"+700+100")

    icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "icons", "main_ico.ico")
    icon_path = os.path.normpath(icon_path)

    #window.iconbitmap(icon_path)

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
    
    flammability_Scale = Scale(scale_box, label="Flammability", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=flammability,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    flammability_Scale.grid(row=0, column=0, padx=(10,5),pady=(10,5))
    
    explosiveness_Scale = Scale(scale_box, label="Explosiveness", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=explosiveness,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    explosiveness_Scale.grid(row=0, column=1, padx=(5,10),pady=(10,5))
    
    particleSpacing_Scale = Scale(scale_box, label="Particle spacing", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=particleSpacing,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    particleSpacing_Scale.grid(row=1, column=0, padx=(10,5),pady=5)
    
    boilPoint_Scale = Scale(scale_box, label="Boil point", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=boilPoint,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    boilPoint_Scale.grid(row=1, column=1, padx=(5,10),pady=5)
    
    temperature_Scale = Scale(scale_box, label="Temperature", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=temperature,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    temperature_Scale.grid(row=2, column=0, padx=(10,5),pady=5)
    
    heatCapacity_Scale = Scale(scale_box, label="Heat capacity", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=heatCapacity,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    heatCapacity_Scale.grid(row=2, column=1, padx=(5,10),pady=5)
    
    viscosity_Scale = Scale(scale_box, label="Viscosity", from_=0, to=100, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=30, variable=viscosity,bg = dark_color_1,fg = whiteColor,font=CTkFont(size = 18),length=200)
    viscosity_Scale.grid(row=3, column=0, padx=(10,5),pady=5)
    
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
        color: '{liquid.color}',
        gasColor: '{liquid.gasColor}',
        barColor: '{liquid.barColor}',
        lightColor: '{liquid.lightColor}',
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
