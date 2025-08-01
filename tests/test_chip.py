from __future__ import annotations

from src.chips.builtins.and_chip import AndChip
from src.chips.builtins.not_chip import NotChip
from src.chips.builtins.or_chip import OrChip
from src.chips.chip import Chip
from src.chips.chip_loader import ChipLoader
from src.chips.chip_part import ChipPart
from src.chips.chipI import ChipI


class MockLoader:
    def load(self, name: str) -> ChipI:
        chip = Chip(
            ["a", "b"],
            ["out"],
            [
                ChipPart("Not", {"in": "a"}, {"out": "nota"}, NotChip()),
                ChipPart("Not", {"in": "b"}, {"out": "notb"}, NotChip()),
                ChipPart("And", {"a": "a", "b": "notb"}, {"out": "w1"}, AndChip()),
                ChipPart("And", {"a": "nota", "b": "b"}, {"out": "w2"}, AndChip()),
                ChipPart("Or", {"a": "w1", "b": "w2"}, {"out": "out"}, OrChip()),
            ],
        )

        return chip


def test_should_create_and_chip() -> None:
    chip = ChipLoader().load("And")
    assert not chip.run({"a": True, "b": False})["out"]


def test_should_create_or_chip() -> None:
    chip = ChipLoader().load("Or")
    assert chip.run({"a": True, "b": False})["out"]


def test_should_create_not_chip() -> None:
    chip = ChipLoader().load("Not")
    assert not chip.run({"in": True})["out"]


def test_should_create_nand_chip() -> None:
    chip = ChipLoader().load("Nand")
    assert chip.run({"a": True, "b": False})["out"]


def test_should_create_xor_chip() -> None:
    chip = MockLoader().load("Xor")
    assert chip.run({"a": True, "b": False})["out"]
    assert chip.run({"a": False, "b": True})["out"]
    assert not chip.run({"a": False, "b": False})["out"]
    assert not chip.run({"a": True, "b": True})["out"]
