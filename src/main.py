from src.chips.chip_loader import ChipLoader
from src.parsers.hdl_reader import HDLReader

hdl_reader = HDLReader(dir_name="hdl_files")
loader = ChipLoader(hdl_reader)
chip = loader.load("Xor")
print(chip.run({"a": True, "b": False})["out"])
print(chip.run({"a": False, "b": True})["out"])
print(chip.run({"a": False, "b": False})["out"])
print(chip.run({"a": True, "b": True})["out"])
