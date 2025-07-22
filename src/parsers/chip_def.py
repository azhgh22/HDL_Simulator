from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class ChipDef:
    name: str
    inputs: List[str]
    outputs: List[str]
    parts: List[Dict[Any, Any]]
