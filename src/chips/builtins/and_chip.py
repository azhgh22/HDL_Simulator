class AndChip:
    def run(self, inputs: dict[str, bool]) -> dict[str, bool]:
        return {"out": inputs["a"] and inputs["b"]}
