import os

from src.chips.chip_part import ChipPart
from src.parsers.hdl_parser import HDLParser


class HDLReader:
    def __init__(self, dir_name: str = "", parser: HDLParser = HDLParser()) -> None:
        self.abs_path = dir_name
        self.parser = parser
        self.inputs: list[str] = []
        self.outputs: list[str] = []
        self.parts: list[ChipPart] = []

    def read(self, name: str) -> None:
        file_path = os.path.join(self.abs_path, name + ".hdl")
        chip_info = self.parser.parse(file_path)
        self.inputs = chip_info.inputs
        self.outputs = chip_info.outputs
        self.parts = []
        for part in chip_info.parts:
            name = part["type"]
            input_dict = part["connections"]
            self.parts.append(ChipPart(name, input_dict, {}, None))

    def get_inputs(self) -> list[str]:
        return self.inputs

    def get_outputs(self) -> list[str]:
        return self.outputs

    def get_parts(self) -> list[ChipPart]:
        return self.parts
