from src.chips.chip_part import ChipPart


class Chip:
    def __init__(self, ins: list[str], outs: list[str], parts: list[ChipPart]) -> None:
        self.ins = ins
        self.outs = outs
        self.parts = parts  # {'a' = a,b=b}, {out=out} chip
        self.part_list = []  # topologically sorted list[Chip]

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        variable_bank = {}
        for key, value in inputs.items():
            variable_bank[key] = value

        for part in self.parts:
            part_input = {}
            for key, value in part.input_dict.items():
                part_input[key] = variable_bank[value]

            result = part.chip.run(part_input)
            # update variable bank
            for key, value in part.out_dict.items():
                variable_bank[value] = result[key]

        ans = {}
        for out_name in self.outs:
            ans[out_name] = variable_bank[out_name]

        return ans
