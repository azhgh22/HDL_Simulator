from src.chips.chip_loader import ChipLoader
from src.parsers.hdl_parser import HDLParser
from src.parsers.hdl_reader import HDLReader

# Not(in=a, out=notA);
# Not(in=b, out=notB);
# And(a=notA, b=b, out=notAandB);
# And(a=notB, b=a, out=notBandA);
# Or(a=notAandB, b=notBandA, out=out);


def test_should_parse_xor_file() -> None:
    file = "hdl_files/Xor.hdl"
    parser = HDLParser()
    chip = parser.parse(file)
    assert chip.name == "Xor"
    assert chip.inputs == ["a", "b"]
    assert chip.outputs == ["out"]
    assert chip.parts == [
        {
            "type": "Not",
            "connections": {"in": "a", "out": "notA"},
        },
        {
            "type": "Not",
            "connections": {"in": "b", "out": "notB"},
        },
        {
            "type": "And",
            "connections": {"a": "notA", "b": "b", "out": "notAandB"},
        },
        {
            "type": "And",
            "connections": {"a": "notB", "b": "a", "out": "notBandA"},
        },
        {
            "type": "Or",
            "connections": {"a": "notAandB", "b": "notBandA", "out": "out"},
        },
    ]


def test_everypart() -> None:
    hdl_reader = HDLReader(dir_name="hdl_files/")
    loader = ChipLoader(hdl_reader)
    chip = loader.load("Xor")
    assert chip.run({"a": True, "b": False})["out"]
    assert chip.run({"a": False, "b": True})["out"]
    assert not chip.run({"a": False, "b": False})["out"]
    assert not chip.run({"a": True, "b": True})["out"]
