import pandas as pd

from src.chips.chip_loader import ChipLoader
from src.testers.hdl_tester import HDLTester
from tests.test_chip_loader import MockReader


class MockXorChip:
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": inputs["a"] ^ inputs["b"]}

    def get_inputs(self) -> list[str]:
        return ["a", "b"]

    def get_outputs(self) -> list[str]:
        return ["out"]


# a b   out result  status
# 0 0   0   1       Fail
# 0 1   1   1       Pass
# 1 0   1   1       Pass
# 1 1   0   0       Pass


def test_should_check_xor_chip() -> None:
    chip = MockXorChip()
    test_frame = pd.DataFrame(
        [
            [False, False, False],
            [False, True, True],
            [True, False, True],
            [True, True, False],
        ],
        columns=["a", "b", "out"],
    )

    tester = HDLTester(chip, test_frame)
    result = tester.check()
    assert result.iloc[0]["result_out"] == test_frame.iloc[0]["out"]
    assert result.iloc[1]["result_out"] == test_frame.iloc[1]["out"]
    assert result.iloc[2]["result_out"] == test_frame.iloc[2]["out"]
    assert result.iloc[3]["result_out"] == test_frame.iloc[3]["out"]


def test_should_fail() -> None:
    chip = MockXorChip()
    test_frame = pd.DataFrame(
        [
            [False, False, True],
            [False, True, True],
            [True, False, True],
            [True, True, False],
        ],
        columns=["a", "b", "out"],
    )

    tester = HDLTester(chip, test_frame)
    result = tester.check()
    assert result.iloc[0]["result_out"] != test_frame.iloc[0]["out"]
    assert result.iloc[1]["result_out"] == test_frame.iloc[1]["out"]
    assert result.iloc[2]["result_out"] == test_frame.iloc[2]["out"]
    assert result.iloc[3]["result_out"] == test_frame.iloc[3]["out"]


def test_should_check_real_chip() -> None:
    loader = ChipLoader(MockReader())
    chip = loader.load("Xor")
    test_frame = pd.DataFrame(
        [
            [False, False, False],
            [False, True, True],
            [True, False, True],
            [True, True, False],
        ],
        columns=["a", "b", "out"],
    )

    tester = HDLTester(chip, test_frame)
    result = tester.check()
    # .iloc[4]['col']
    assert result.iloc[0]["result_out"] == test_frame.iloc[0]["out"]
    assert result.iloc[1]["result_out"] == test_frame.iloc[1]["out"]
    assert result.iloc[2]["result_out"] == test_frame.iloc[2]["out"]
    assert result.iloc[3]["result_out"] == test_frame.iloc[3]["out"]
