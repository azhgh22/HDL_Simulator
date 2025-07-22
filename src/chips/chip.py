from src.chips.chip_part import ChipPart


class Chip:
    def __init__(self, ins: list[str], outs: list[str], parts: list[ChipPart]) -> None:
        self.ins = ins
        self.outs = outs
        self.parts = parts  # {'a' = a,b=b}, {out=out} chip

    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        variable_bank = {}
        for key, value in inputs.items():
            variable_bank[key] = value

        for part in self.parts:
            part_input = {}
            for key1, value1 in part.input_dict.items():
                part_input[key1] = variable_bank[value1]

            if part.chip is None:
                continue
            result = part.chip.run(part_input)
            # update variable bank
            for key2, value2 in part.out_dict.items():
                variable_bank[value2] = result[key2]

        ans = {}
        for out_name in self.outs:
            ans[out_name] = variable_bank[out_name]

        return ans

    def get_inputs(self) -> list[str]:
        return self.ins

    def get_outputs(self) -> list[str]:
        return self.outs
