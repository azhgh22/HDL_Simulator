class NotChip:
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": not inputs["a"]}
