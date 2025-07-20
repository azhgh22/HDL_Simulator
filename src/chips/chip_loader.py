from chips.chip import Chip
from src.chips.builtins.and_chip import AndChip
from src.chips.builtins.nand_chip import NandChip
from src.chips.builtins.not_chip import NotChip
from src.chips.builtins.or_chip import OrChip
from src.chips.chip_part import ChipPart
from src.chips.chipI import ChipI


class HDLReader:
    def read(self, name: str) -> None:
        pass

    def get_inputs(self) -> list[str]:
        pass

    def get_outputs(self) -> list[str]:
        pass

    def get_parts(self) -> list[ChipPart]:
        pass


class ChipLoader:
    def __init__(self) -> None:
        self.chip_dict: dict[str, ChipI] = {
            "And": AndChip(),
            "Or": OrChip(),
            "Not": NotChip(),
            "Nand": NandChip(),
        }

    def load(self, name: str) -> ChipI:
        d = self.chip_dict
        if name in d.keys():
            return d[name]

        reader = HDLReader()
        reader.read()
        inputs = reader.get_inputs()
        outputs = reader.get_outputs()
        parts = reader.get_parts()

        for part in parts:
            child = self.load(part.name)
            self.chip_dict[part.name] = child
            part.chip = child

        chip = Chip(inputs, outputs, parts)

        return chip
