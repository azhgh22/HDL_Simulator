import numpy as np
import pandas as pd

from src.chips.chipI import ChipI


class HDLTester:
    def __init__(self, chip: ChipI, test_frame: pd.DataFrame) -> None:
        self.chip = chip
        self.test = test_frame

    def check(self) -> pd.DataFrame:
        ans = pd.DataFrame()
        chip_input = self.chip.get_inputs()
        inputs = {}
        for c in chip_input:
            inputs[c] = self.test[c]

        result = self.chip.run(inputs)
        status = pd.DataFrame([True] * self.test.shape[0])
        for out in self.chip.get_outputs():
            ans[f"expected_{out}"] = self.test[out]
            ans[f"result_{out}"] = result[out]
            temp = pd.DataFrame(ans[f"expected_{out}"] == ans[f"result_{out}"])
            status = status & temp

        ans["status"] = np.where(status, "Pass", "Fail")
        return ans

    def make_report(self, result: pd.DataFrame) -> None:
        inputs = self.chip.get_inputs()
        outs = self.chip.get_outputs()
        passed = result["status"].value_counts().get("Pass", 0)
        for i in range(result.shape[0]):
            row = result.iloc[i]
            print(f"Test case {i + 1}: {row['status']}")
            rep = "Inputs: "
            for inp in inputs:
                rep = rep + f"{inp}={self.test.iloc[i][inp]} "

            rep = rep + "→ Output: "
            for out in outs:
                rep = rep + f"expected_{out}={self.test.iloc[i][out]} "
                rep = rep + f"your_{out}={result.iloc[i][f'result_{out}']} "
            print(f"    {rep}")

        print(f"Passed {passed}/{result.shape[0]} tests")
