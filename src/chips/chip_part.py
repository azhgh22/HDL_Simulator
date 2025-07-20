from dataclasses import dataclass

from src.chips.chipI import ChipI


@dataclass
class ChipPart:
    name: str
    input_dict: dict[str, str]
    out_dict: dict[str, str]
    chip: ChipI | None
