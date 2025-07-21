import numpy as np
import pandas as pd

from src.chips.chipI import ChipI


class HDLTester:
    def __init__(self, chip: ChipI, test_frame: pd.DataFrame) -> None:
        self.chip = chip
        self.test = test_frame

    def check(self) -> pd.DataFrame:
        ans = self.test.copy()
        chip_input = self.chip.get_inputs()
        inputs = {}
        for c in chip_input:
            inputs[c] = self.test[c]

        result = self.chip.run(inputs)
        ans["result"] = result["out"]
        ans["status"] = np.where(ans["out"] == ans["result"], "Pass", "Fail")

        return ans

    def make_report(self) -> None:
        pass
