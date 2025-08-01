import re
from typing import Any, Dict

from src.parsers.chip_def import ChipDef


class HDLParser:
    def __clean_lines(self, lines: list[str]) -> list[str]:
        # Join all lines for block comment removal
        code = "\n".join(lines)

        # Remove multiline comments: /* ... */
        code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)

        # Remove single-line comments: //
        code = re.sub(r"//.*", "", code)

        # Return cleaned and non-empty lines
        return [line.strip() for line in code.splitlines() if line.strip()]

    def __parse_part_line(self, line: str) -> Dict[Any, Any]:
        line = line.rstrip(";")

        chip_type, rest = line.split("(", 1)
        chip_type = chip_type.strip()

        conn_str = rest.rstrip(")")
        connections = {}

        for pair in conn_str.split(","):
            left, right = map(str.strip, pair.split("="))
            connections[left] = right

        return {"type": chip_type, "connections": connections}

    def parse(self, file_path: str) -> ChipDef:
        with open(file_path) as f:
            lines = self.__clean_lines(f.readlines())

        # Parse chip name
        chip_match = re.match(r"^CHIP\s+(\w+)\s*{", lines[0])
        if not chip_match:
            raise ValueError("First line must define CHIP")

        chip_name = chip_match.group(1)

        inputs = []
        outputs = []
        parts = []

        in_parts_section = False
        i = 1
        while i < len(lines):
            line = lines[i]

            if line.startswith("IN "):
                in_block = line[len("IN ") :]
                while not in_block.endswith(";"):
                    i += 1
                    in_block += " " + lines[i]
                inputs = [x.strip() for x in in_block.rstrip(";").split(",")]

            elif line.startswith("OUT "):
                out_block = line[len("OUT ") :]
                while not out_block.endswith(";"):
                    i += 1
                    out_block += " " + lines[i]
                outputs = [x.strip() for x in out_block.rstrip(";").split(",")]

            elif line.startswith("PARTS:"):
                in_parts_section = True

            elif in_parts_section:
                if line == "}":
                    break
                parts.append(self.__parse_part_line(line))

            i += 1

        return ChipDef(name=chip_name, inputs=inputs, outputs=outputs, parts=parts)
