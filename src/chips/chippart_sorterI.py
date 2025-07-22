from typing import Protocol

from src.chips.chip_part import ChipPart


class ChipPartSorterI(Protocol):
    def sort(self, parts: list[ChipPart]) -> list[ChipPart]:
        pass
