from __future__ import annotations
from typing import Optional

# Global class for basicly all stuff
class UnlockableContent:
    def __init__(self, localizedName: str, description: str, details: str, alwaysUnlocked: bool, inlineDescription: bool, hideDetails: bool, generateIcons: bool, iconId: int, selectionSize: float, fullOverride: str):
        self.localizedName = localizedName
        self.description = description
        self.details = details
        self.alwaysUnlocked = alwaysUnlocked
        self.inlineDescription = inlineDescription
        self.hideDetails = hideDetails
        self.generateIcons = generateIcons
        self.iconId = iconId
        self.selectionSize = selectionSize
        # self.uiIcon = uiIcon
        #self.fullIcon = fullIcon
        self.fullOverride = fullOverride
        # self.techNode = techNode
        # self.techNodes = techNodes

# For the tech tree - TODO: work in progress
class techNode:
    pass

# For the items 
class Item:
    def __init__(self, name: str, color: hex, explosiveness: float, flammability: float, radioactivity: float, charge: float, hardness: int, cost: float, healthScaling: float, lowPriority: bool, frames: int, transitionFrames: int, frameTime: float, buildable: bool, hidden: bool, hiddenOnPlanets: list):
        self.name = name
        self.color = color
        self.explosiveness = explosiveness
        self.flammability = flammability
        self.radioactivity = radioactivity
        self.charge = charge
        self.hardness = hardness
        self.cost = cost
        self.healthScaling = healthScaling
        self.lowPriority = lowPriority
        self.frames = frames
        self.transitionFrames = transitionFrames
        self.frameTime = frameTime
        self.buildable = buildable
        self.hidden = hidden
        self.hiddenOnPlanets = hiddenOnPlanets

# for stacks specifically
class ItemStack:
    def __init__(self, item: Item, count: int):
        self.item = item
        self.count = count

# for the liquids
class Liquid:
    def __init__(self, name: str, image_path, color: hex, gasColor: hex, barColor: hex, lightColor: hex, flammability: float, explosiveness: float ,hidden: bool, canStayOn: list[Liquid] = None, blockReactive = True, coolant = True, moveThroughBlocks = False, incinerate = True, effect = "StatusEffects.none", particleEffect = "Fx.none", particleSpacing = 60.0, boilPoint = 2.0, capPuddles = True, vaporEffect = "Fx.vapor", temperature = 0.5, heatCapacity = 0.5, viscosity = 0.5, animationFrames = 50, animationScaleGas = 190.0, animationScaleLiquid = 230.0, gas = False):
        self.name = name
        self.image_path = image_path
        self.color = color
        self.gasColor = gasColor
        self.barColor = barColor
        self.lightColor = lightColor
        self.flammability = flammability
        self.explosiveness = explosiveness
        self.hidden = hidden
        self.canStayOn = canStayOn
        self.blockReactive = blockReactive
        self.coolant = coolant
        self.moveThroughBlocks = moveThroughBlocks
        self.incinerate = incinerate
        self.effect = effect
        self.particleEffect = particleEffect
        self.particleSpacing = particleSpacing
        self.boilPoint = boilPoint
        self.capPuddles = capPuddles
        self.vaporEffect = vaporEffect
        self.temperature = temperature
        self.heatCapacity = heatCapacity
        self.viscosity = viscosity
        self.animationFrames = animationFrames
        self.animationScaleGas = animationScaleGas
        self.animationScaleLiquid = animationScaleLiquid
        self.gas = gas

# for the stack of liquids (yes in mindustry it exist)
class LiquidStack:
    def __init__(self, liquid: Liquid, amount: float):
        self.liquid = liquid
        self.amount = amount