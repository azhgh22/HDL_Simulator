from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ChipDef:
    name: str
    inputs: List[str]
    outputs: List[str]
    parts: List[Dict]
