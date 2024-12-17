from __future__ import annotations
from typing import Optional

from .unlockableContent import UnlockableContent

class Item(UnlockableContent):
    def __init__(self, name: str, color: hex, explosiveness: float, flammability: float, radioactivity: float, charge: float, hardness: int, cost: float, healthScaling: float,
                        lowPriority: bool, frames: int, transitionFrames: int, frameTime: float, buildable: bool, hidden: bool, hiddenOnPlanets: list, localizedName: str, description: str,
                        details: str, alwaysUnlocked: bool, inlineDescription: bool, hideDetails: bool, generateIcons: bool, iconId: int, selectionSize: float, fullOverride: str) -> None:
        
        super().__init__(localizedName, description, details, alwaysUnlocked, inlineDescription,
                        hideDetails, generateIcons, iconId, selectionSize, fullOverride)
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