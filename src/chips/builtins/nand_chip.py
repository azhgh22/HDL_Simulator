import pandas as pd

from src.chips.chip import Chip


class NandChip(Chip):
    def __init__(self) -> None:
        super().__init__(["a", "b"], ["out"], [])

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        if isinstance(inputs["a"], (pd.Series, pd.DataFrame)):
            return {"out": ~(inputs["a"] & inputs["b"])}
        return {"out": not (inputs["a"] and inputs["b"])}
