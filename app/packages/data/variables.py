from __future__ import annotations
from typing import Optional

# mindustry class
from .mindustry_class.Item import *
from .mindustry_class.Liquid import *
from .mindustry_class.unlockableContent import UnlockableContent

# Main parameters
UC_list: list[UnlockableContent] = []

# synchronizing unlockableContent with all other things
id_list: list[dict] = []

# Lists of all things
item_list: list[Item] = []
liquid_list: list[Liquid] = []

# Mod already created
already_packed: bool = False