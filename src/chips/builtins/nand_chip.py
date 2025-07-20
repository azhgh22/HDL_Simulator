from src.chips.chip import Chip


class NandChip(Chip):
    def __init__(self) -> None:
        super().__init__(["a", "b"], ["out"], [])

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": not (inputs["a"] and inputs["b"])}
