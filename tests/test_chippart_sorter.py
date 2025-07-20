from src.chips.chip_part import ChipPart
from src.chips.chippart_sorter import ChipPartSorter


def test_should_sort_parts() -> None:
    parts = [
        ChipPart("Or", {"a": "w1", "b": "w2"}, {"out": "out"}, None),
        ChipPart("X", {"a": "a", "b": "b"}, {"out": "w1"}, None),
        ChipPart("X", {"a": "b", "b": "a"}, {"out": "w2"}, None),
    ]

    assert parts[0].name == "Or"
    assert parts[1].name == "X"
    assert parts[2].name == "X"

    sorter = ChipPartSorter()
    parts = sorter.sort(parts)

    assert parts[0].name == "X"
    assert parts[1].name == "X"
    assert parts[2].name == "Or"
