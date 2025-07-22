from src.chips.chip import Chip
from src.chips.chip_loader import ChipLoader
from src.chips.chip_part import ChipPart


class MockReader:
    def __init__(self) -> None:
        self.X = Chip(
            ["a", "b"],
            ["out"],
            [
                ChipPart("And", {"a": "a", "b": "notb", "out": "out"}, {}, None),
                ChipPart("Not", {"in": "b", "out": "notb"}, {}, None),
            ],
        )

        self.Xor = Chip(
            ["a", "b"],
            ["out"],
            [
                ChipPart("Or", {"a": "w1", "b": "w2", "out": "out"}, {}, None),
                ChipPart("X", {"a": "a", "b": "b", "out": "w1"}, {}, None),
                ChipPart("X", {"a": "b", "b": "a", "out": "w2"}, {}, None),
            ],
        )
        self.name = ""

    def read(self, name: str) -> None:
        self.name = name

    def get_inputs(self) -> list[str]:
        if self.name == "X":
            return self.X.ins
        else:
            return self.Xor.ins

    def get_outputs(self) -> list[str]:
        if self.name == "X":
            return self.X.outs
        else:
            return self.Xor.outs

    def get_parts(self) -> list[ChipPart]:
        if self.name == "X":
            return self.X.parts
        else:
            return self.Xor.parts


# CHIP X {
#     IN a, b;
#     OUT out;

#     PARTS:
#     Not(a=b, out=notb);
#     And(a=a, b=notb, out=out);
# }


# CHIP Xor {
#     IN a, b;
#     OUT out;

#     PARTS:
#     X(a=a,b=b,out=w1)
#     X(a=b,b=a,out=w2)
#     Or(a=w1, b=w2, out=out);
# }


def test_should_create_deep_chip() -> None:
    loader = ChipLoader(MockReader())
    chip = loader.load("Xor")
    assert chip.run({"a": True, "b": False})["out"]
    assert chip.run({"a": False, "b": True})["out"]
    assert not chip.run({"a": False, "b": False})["out"]
    assert not chip.run({"a": True, "b": True})["out"]
