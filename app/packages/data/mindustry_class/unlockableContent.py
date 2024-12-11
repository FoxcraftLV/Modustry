from __future__ import annotations
from typing import Optional

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
