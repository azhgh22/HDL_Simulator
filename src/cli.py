import os
from pathlib import Path

import pandas as pd

from src.chips.chip_loader import ChipLoader
from src.parsers.hdl_reader import HDLReader
from src.testers.hdl_tester import HDLTester


class CLI:
    def run(self) -> None:
        hdl_file, test_file = self.read_input()
        hdl_path = Path(hdl_file)

        hdl_reader = HDLReader(dir_name=hdl_path.parent)
        loader = ChipLoader(hdl_reader)
        chip = loader.load(hdl_path.stem)
        chip_tester = HDLTester(chip, self.read_csv(test_file))
        result = chip_tester.check()
        chip_tester.make_report(result)

    def read_input(self) -> tuple[str, str]:
        hdl_file = input("enter path of hdl file: ")
        test_file = input("enter path of test file: ")
        return hdl_file, test_file

    def read_csv(self, test_file: str) -> pd.DataFrame:
        with open(test_file) as f:
            lines = [line.replace(";", ",") for line in f]

        with open("cleaned.csv", "w") as f:
            f.writelines(lines)

        data = pd.read_csv("cleaned.csv")
        os.remove("cleaned.csv")
        return data
