from __future__ import annotations
from typing import Optional

from .unlockableContent import UnlockableContent

# for the liquids
class Liquid(UnlockableContent):
    def __init__(self, name: str, localizedName: str, description: str, details: str, alwaysUnlocked: bool, 
                inlineDescription: bool, hideDetails: bool, generateIcons: bool, iconId: int, 
                selectionSize: float, fullOverride: str, image_path, color: str, gasColor: str, barColor: str, 
                lightColor: str, flammability: float, explosiveness: float ,hidden: bool, 
                canStayOn: list[Liquid] = None, blockReactive = True, coolant = True, 
                moveThroughBlocks = False, incinerate = True, effect = "StatusEffects.none", 
                particleEffect = "Fx.none", particleSpacing = 60.0, boilPoint = 2.0, capPuddles = True, 
                vaporEffect = "Fx.vapor", temperature = 0.5, heatCapacity = 0.5, viscosity = 0.5, 
                animationFrames = 50, animationScaleGas = 190.0, animationScaleLiquid = 230.0, gas = False, ):
        super().__init__(localizedName, description, details, alwaysUnlocked, inlineDescription,
                        hideDetails, generateIcons, iconId, selectionSize, fullOverride)
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
    
    def __str__(self) -> str:
        return "Liquid"

# for the stack of liquids (yes in mindustry it exist)
class LiquidStack:
    def __init__(self, liquid: Liquid, amount: float):
        self.liquid = liquid
        self.amount = amount