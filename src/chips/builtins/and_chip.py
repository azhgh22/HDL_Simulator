from src.chips.chip import Chip


class AndChip(Chip):
    def __init__(self) -> None:
        super().__init__(["a", "b"], ["out"], [])

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": inputs["a"] and inputs["b"]}
