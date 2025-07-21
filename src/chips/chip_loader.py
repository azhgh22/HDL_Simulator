from src.chips.builtins.and_chip import AndChip
from src.chips.builtins.nand_chip import NandChip
from src.chips.builtins.not_chip import NotChip
from src.chips.builtins.or_chip import OrChip
from src.chips.chip import Chip
from src.chips.chipI import ChipI
from src.chips.chippart_sorter import ChipPartSorter
from src.parsers.hdl_reader import HDLReader


class ChipLoader:
    def __init__(self, reader=HDLReader(), sorter=ChipPartSorter()) -> None:
        self.chip_dict: dict[str, ChipI] = {
            "And": AndChip(),
            "Or": OrChip(),
            "Not": NotChip(),
            "Nand": NandChip(),
        }
        self.reader = reader
        self.sorter = sorter

    def load(self, name: str) -> ChipI:
        d = self.chip_dict
        if name in d.keys():
            return d[name]

        self.reader.read(name)
        inputs = self.reader.get_inputs()
        outputs = self.reader.get_outputs()
        parts = self.reader.get_parts()

        for part in parts:
            child = self.load(part.name)
            self.chip_dict[part.name] = child
            part.chip = child
            outs = child.get_outputs()
            for o in outs:
                part.out_dict[o] = part.input_dict[o]
                part.input_dict.pop(o)

        parts = self.sorter.sort(parts)

        chip = Chip(inputs, outputs, parts)

        return chip
