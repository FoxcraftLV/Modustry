from __future__ import annotations
from typing import Optional

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