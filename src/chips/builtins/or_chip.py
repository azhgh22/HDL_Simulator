class OrChip:
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": inputs["a"] or inputs["b"]}
