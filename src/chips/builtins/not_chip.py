import pandas as pd

from src.chips.chip import Chip


class NotChip(Chip):
    def __init__(self) -> None:
        super().__init__(["in"], ["out"], [])

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        if isinstance(inputs["in"], (pd.Series, pd.DataFrame)):
            return {"out": ~inputs["in"]}
        return {"out": not inputs["in"]}
