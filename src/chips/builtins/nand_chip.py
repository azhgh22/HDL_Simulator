class NandChip:
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": not (inputs["a"] and inputs["b"])}
