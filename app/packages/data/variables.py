from __future__ import annotations
from typing import Optional

from .mindustry_class import *

# Main parameters
UC_list: list[UnlockableContent] = []

# synchronizing unlockableContent with all other things
id_list: list[dict] = []

# Lists of all things
item_list: list[Item] = []

# Mod already created
already_packed: bool = False