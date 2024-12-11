# Screen modules
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Data modules
from ..data.variables import item_list, UC_list, id_list
from .global_func import choose_color

# Mindustry class
from ..data.mindustry_class.unlockableContent import UnlockableContent
from ..data.mindustry_class.Item import Item

def item_creator(root: Tk)->None:
    ##### Variables #####
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
    
    # Window
    window = Toplevel(root)
    window.title("Item Creator")
    # window.iconbitmap("logo.ico")
    
    # Label frames
    UC_box = LabelFrame(window, text="Global Properties")
    UC_box.grid(row=0, column=0)
    
    item_box = LabelFrame(window, text="Item properties")
    item_box.grid(row=0, column=1)
    
    # Image loader
    picture_path = filedialog.askopenfilename(title="Select your sprite (48x48 recommended)", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    picture = ImageTk.PhotoImage(Image.open(picture_path).resize((256, 256), Image.NEAREST))
    
    picture_box = Label(window, image=picture)
    picture_box._strong_ref_image = picture
    picture_box.grid(row=0, column=2)
    
    ##### Unlockable Content parameters #####
    name_box = LabelFrame(UC_box)
    name_box.pack(side=TOP)
    name_Label = Label(name_box, text="Identification Name: ")
    name_Entry = Entry(name_box, textvariable=name)
    name_Label.pack(side=LEFT)
    name_Entry.pack(side=LEFT)
    
    description_box = LabelFrame(UC_box)
    description_box.pack(side=TOP)
    description_Label = Label(description_box, text="Main description: ")
    description_Text = Text(description_box, height=5, width=20)
    description_Label.pack(side=LEFT)
    description_Text.pack(side=LEFT)
    description_Scrollbar = Scrollbar(description_box, orient=VERTICAL, command=description_Text.yview)
    description_Scrollbar.pack(side=LEFT)
    
    localizedName_box = LabelFrame(UC_box)
    localizedName_box.pack(side=TOP)
    localizedName_Label = Label(localizedName_box, text="Name in-game")
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
    
    
    ### Item parameters #####
    color_Button = Button(item_box, text="Choose the color", command=lambda: color.set((choose_color(window, color_Button))))
    color_Button.pack(side=TOP)
    
    scale_box = LabelFrame(item_box)
    scale_box.pack(side=TOP)
    
    explosiveness_Scale = Scale(scale_box, label="Explosiveness", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=explosiveness)
    explosiveness_Scale.grid(row=0, column=0)
    
    flammability_Scale = Scale(scale_box, label="Flammability", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=flammability)
    flammability_Scale.grid(row=0, column=1)
    
    radioactivity_Scale = Scale(scale_box, label="Radioactivity", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=radioactivity)
    radioactivity_Scale.grid(row=1, column=0)
    
    charge_Scale = Scale(scale_box, label="Charge", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=charge)
    charge_Scale.grid(row=1, column=1)
    
    hardness_Scale = Scale(scale_box, label="Hardness", from_=0, to=10, tickinterval=5, resolution=1, orient=HORIZONTAL, sliderlength=10, variable=hardness)
    hardness_Scale.grid(row=2, column=0)
    
    cost_Scale = Scale(scale_box, label="Cost", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=cost)
    cost_Scale.grid(row=2, column=1)
    
    healthScaling_Scale = Scale(scale_box, label="Health Scaling", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=healthScaling)
    healthScaling_Scale.grid(row=3, column=0)
    
    frames_Scale = Scale(scale_box, label="Frames", from_=0, to=60, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=10, variable=frames)
    frames_Scale.grid(row=3, column=1)
    
    transitionFrames_Scale = Scale(scale_box, label="Transition frames", from_=0, to=60, tickinterval=25, resolution=1, orient=HORIZONTAL, sliderlength=10, variable=transitionFrames)
    transitionFrames_Scale.grid(row=4, column=0)
    
    frameTime_Scale = Scale(scale_box, label="Frame time", from_=0, to=10, tickinterval=5, resolution=0.1, orient=HORIZONTAL, sliderlength=10, variable=frameTime)
    frameTime_Scale.grid(row=4, column=1)
    
    #TODO: hiddenOnPlanets
    
    check_box = LabelFrame(item_box)
    check_box.pack(side=TOP)
    lowPriority_Check = Checkbutton(check_box, text="Low Priority", variable=lowPriority, offvalue="false", onvalue="true")
    lowPriority_Check.grid(row=0, column=0)
    buildable_Check = Checkbutton(check_box, text="Is buildable", variable=buildable, offvalue="false", onvalue="true")
    buildable_Check.grid(row=0, column=1)
    hidden_Check = Checkbutton(check_box, text="Is hidden", variable=hidden, offvalue="false", onvalue="true")
    hidden_Check.grid(row=1, column=0)
    
    saveButton = Button(window, text="Save", command=lambda: create_item(
        window,
        Item(
            name.get(),
            color.get()[1:],
            explosiveness.get(),
            flammability.get(),
            radioactivity.get(),
            charge.get(),
            hardness.get(),
            cost.get(),
            healthScaling.get(),
            frames.get(),
            transitionFrames.get(),
            frameTime.get(),
            lowPriority.get(),
            buildable.get(),
            hidden.get(),
            hiddenOnPlanets,
        ),
        UnlockableContent(
            localizedName.get(),
            description_Text.get(index1='1.0', index2=END).strip(),
            details.get(),
            alwaysUnlocked.get(),
            inlineDescription.get(),
            hideDetails.get(),
            generateIcons.get(),
            iconId.get(),
            selectionSize.get(),
            fullOverride.get()
        ),
        picture_path
    ))
    saveButton.grid(row=1, column=0)
    
    # Show the window
    window.lift()
    window.pack_propagate()

def create_item(master: Toplevel, localItem: Item, localContent: UnlockableContent, image_path)->None:
    global item_list, UC_list, id_list
    item_list.append(localItem)
    UC_list.append(localContent)
    # TODO: Make a better way to store id_list
    id_list.append({'name': localItem.name, 'item_id': item_list.index(localItem), 'UC_id': UC_list.index(localContent), 'image_path': image_path})
    print(item_list)
    print(UC_list)
    print(id_list)
    
    print("Item added successfully")
    master.destroy()

def create_hjson_item_file(item: Item, unlockablecontent: UnlockableContent):
    hjson = f"""
    {{
        type: Item,
        name: '{item.name}',
        localizedName: '{unlockablecontent.localizedName}',
        description: '{unlockablecontent.description}',
        detail: '{unlockablecontent.details}',
        alwaysUnlocked: {unlockablecontent.alwaysUnlocked},
        inlineDescription: {unlockablecontent.inlineDescription},
        hideDetails: {unlockablecontent.hideDetails},
        generateIcons: {unlockablecontent.generateIcons},
        iconId: {unlockablecontent.iconId},
        selectionSize: {unlockablecontent.selectionSize},
        fullOverride: {unlockablecontent.fullOverride},
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
