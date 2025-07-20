from collections import deque

from src.chips.chip_part import ChipPart


class ChipPartSorter:
    def sort(self, parts: list[ChipPart]) -> list[ChipPart]:
        in_count = [0] * len(parts)
        graph = self.create_graph(parts, in_count)
        print(graph)
        print(in_count)
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

    def create_graph(
        self, parts: list[ChipPart], in_count: list[int]
    ) -> list[list[int]]:
        ans = []

        for i in range(len(parts)):
            neigs = []
            for j in range(len(parts)):
                if i == j:
                    continue

                outs = parts[i].out_dict.values()
                # print(outs)
                ins = parts[j].input_dict.values()
                # print(ins)

                if self.has_intersection(outs, ins):
                    in_count[j] = in_count[j] + 1
                    neigs.append(j)

            ans.append(neigs)
        return ans

    def has_intersection(self, list1, list2):
        return bool(set(list1) & set(list2))
