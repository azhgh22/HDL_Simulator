from src.chips.chip import Chip


class NotChip(Chip):
    def __init__(self) -> None:
        super().__init__(["a"], ["out"], [])

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": not inputs["a"]}
