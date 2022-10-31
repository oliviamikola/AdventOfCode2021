from typing import Tuple

from DayBase import DayBase, DayBaseSmall


class Day5(DayBase):
    def __init__(self):
        DayBase.__init__(self, 5, to_int=False)

        self.vent_ranges = []
        for line in self.data:
            line = line.replace(" -> ", ",")
            self.vent_ranges.append(line)

    def _find_overlap(self, include_diagonals=False):
        point_counter = {}

        for vent_range in self.vent_ranges:
            x1, y1, x2, y2 = map(int, vent_range.split(','))
            (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])

            if x1 == x2 or y1 == y2:
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if (x, y) not in point_counter:
                            point_counter[(x, y)] = 0
                        point_counter[(x, y)] += 1

            elif include_diagonals:
                if y1 < y2:
                    for index, x in enumerate(range(x1, x2 + 1)):
                        point = (x, y1 + index)

                        if point not in point_counter:
                            point_counter[point] = 0
                        point_counter[point] += 1
                else:
                    for index, x in enumerate(range(x1, x2 + 1)):
                        point = (x, y1 - index)

                        if point not in point_counter:
                            point_counter[point] = 0
                        point_counter[point] += 1

        dangerous_vent_count = 0
        for vent, counter in point_counter.items():
            if counter > 1:
                dangerous_vent_count += 1

        return dangerous_vent_count

    def part1(self):
        return self._find_overlap()

    def part2(self):
        return self._find_overlap(True)


day = Day5()
day.run()
