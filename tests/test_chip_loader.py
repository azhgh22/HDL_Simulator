from src.chips.chip_loader import ChipLoader
from src.chips.chip_part import ChipPart


class MockReader:
    def __init__(self) -> None:
        self.d = {}
        self.d["X"] = {
            "inputs": ["a", "b"],
            "outputs": ["out"],
            "parts": [
                ChipPart("And", {"a": "a", "b": "notb", "out": "out"}, {}, None),
                ChipPart("Not", {"a": "b", "out": "notb"}, {}, None),
            ],
        }

        self.d["Xor"] = {
            "inputs": ["a", "b"],
            "outputs": ["out"],
            "parts": [
                ChipPart("Or", {"a": "w1", "b": "w2", "out": "out"}, {}, None),
                ChipPart("X", {"a": "a", "b": "b", "out": "w1"}, {}, None),
                ChipPart("X", {"a": "b", "b": "a", "out": "w2"}, {}, None),
            ],
        }
        self.name = ""

    def read(self, name: str) -> None:
        self.name = name

    def get_inputs(self) -> list[str]:
        return self.d[self.name]["inputs"]

    def get_outputs(self) -> list[str]:
        return self.d[self.name]["outputs"]

    def get_parts(self) -> list[ChipPart]:
        return self.d[self.name]["parts"]


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


def test_should_create_deep_ship():
    loader = ChipLoader(MockReader())
    chip = loader.load("Xor")
    assert chip.run({"a": True, "b": False})["out"]
    assert chip.run({"a": False, "b": True})["out"]
    assert not chip.run({"a": False, "b": False})["out"]
    assert not chip.run({"a": True, "b": True})["out"]
