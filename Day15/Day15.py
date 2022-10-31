from typing import List, Dict, Tuple, Set
from queue import PriorityQueue
from DayBase import DayBase, DayBaseSmall


class Day15(DayBase):
    def __init__(self):
        DayBase.__init__(self, 15, to_int=False)

        self.start = (0, 0)
        self.end = (len(self.data) - 1, len(self.data) - 1)

        self.weights: Dict[Tuple[int, int], int] = {}
        for row_index, row in enumerate(self.data):
            for column_index, weight in enumerate(row):
                self.weights[(row_index, column_index)] = int(weight)

    def _dijkstra(self, weights: Dict[Tuple[int, int], int], start: Tuple[int, int], end: Tuple[int, int]) -> int:
        def _dijkstra_inner(neighbor: Tuple[int, int], start_weight: int):
            if neighbor not in weights or neighbor in visited:
                return
            visited.add(neighbor)

            current_weight = lowest_weights.get(neighbor)
            point_weight = weights[neighbor] + start_weight

            if current_weight is None or point_weight < current_weight:
                lowest_weights[point] = point_weight
                queue.put((point_weight, neighbor))

        queue = PriorityQueue()
        visited: Set[Tuple[int, int]] = set()
        lowest_weights: Dict[Tuple[int, int], int] = {}

        queue.put((0, start))

        while not queue.empty():
            total_weight, point = queue.get()

            if point == end:
                return total_weight

            x, y = point
            for p in {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}:
                _dijkstra_inner(p, total_weight)

    def part1(self):
        return self._dijkstra(self.weights, self.start, self.end)

    def part2(self):
        new_weights: Dict[Tuple[int, int], int] = {}
        length = self.end[0] + 1
        for row_quadrant in range(5):
            for column_quadrant in range(5):
                for point, weight in self.weights.items():
                    x, y = point
                    new_weights[(x + length * row_quadrant, y + length * column_quadrant)] = \
                        (weight - 1 + row_quadrant + column_quadrant) % 9 + 1

        end = (length * 5 - 1, length * 5 - 1)

        return self._dijkstra(new_weights, self.start, end)



day = Day15()
day.run()
