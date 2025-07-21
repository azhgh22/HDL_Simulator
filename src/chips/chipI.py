from typing import Protocol


class ChipI(Protocol):
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        pass

    def get_inputs(self) -> list[str]:
        pass

    def get_outputs(self) -> list[str]:
        pass
