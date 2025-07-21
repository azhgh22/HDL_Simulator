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
        chip_tester = HDLTester(chip, pd.read_csv(test_file))
        result = chip_tester.check()
        chip_tester.make_report(result)

    def read_input(self) -> tuple[str, str]:
        hdl_file = input("enter path of hdl file: ")
        test_file = input("enter path of test file: ")
        return hdl_file, test_file
