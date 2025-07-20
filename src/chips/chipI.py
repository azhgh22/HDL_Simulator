from typing import Protocol


class ChipI(Protocol):
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        pass
