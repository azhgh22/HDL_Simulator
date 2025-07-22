from collections import deque

from src.chips.chip_part import ChipPart


class ChipPartSorter:
    def sort(self, parts: list[ChipPart]) -> list[ChipPart]:
        in_count = [0] * len(parts)
        graph = self.__create_graph(parts, in_count)
        queue = deque([i for i in range(len(in_count)) if in_count[i] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(parts[node])

            for neighbor in graph[node]:
                in_count[neighbor] -= 1
                if in_count[neighbor] == 0:
                    queue.append(neighbor)

        return result
        # return []

    def __create_graph(
        self, parts: list[ChipPart], in_count: list[int]
    ) -> list[list[int]]:
        ans = []

        for i in range(len(parts)):
            neigs = []
            for j in range(len(parts)):
                if i == j:
                    continue

                outs = list(parts[i].out_dict.values())
                # print(outs)
                ins = list(parts[j].input_dict.values())
                # print(ins)

                if self.__has_intersection(outs, ins):
                    in_count[j] = in_count[j] + 1
                    neigs.append(j)

            ans.append(neigs)
        return ans

    def __has_intersection(self, list1: list[str], list2: list[str]) -> bool:
        return bool(set(list1) & set(list2))
