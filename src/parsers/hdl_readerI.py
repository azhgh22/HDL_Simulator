from typing import Protocol

from src.chips.chip_part import ChipPart


class HDLReaderI(Protocol):
    def read(self, name: str) -> None:
        pass

    def get_inputs(self) -> list[str]:
        pass

    def get_outputs(self) -> list[str]:
        pass

    def get_parts(self) -> list[ChipPart]:
        pass
