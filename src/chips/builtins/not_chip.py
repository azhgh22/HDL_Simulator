import pandas as pd

from src.chips.chip import Chip


class NotChip(Chip):
    def __init__(self) -> None:
        super().__init__(["a"], ["out"], [])

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        if isinstance(inputs["a"], (pd.Series, pd.DataFrame)):
            return {"out": ~inputs["a"]}
        return {"out": not inputs["a"]}
