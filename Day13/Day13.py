import sys
from typing import List, Tuple, Dict
from DayBase import DayBase, DayBaseSmall


class Day13(DayBase):
    def __init__(self):
        DayBase.__init__(self, 13, to_int=False)

        self.max_x = sys.maxsize
        self.max_y = sys.maxsize

        self.points: Dict[Tuple[int, int]] = {}
        self.instructions: List[Tuple[str, int]] = []

        instruction_bool = False
        for line in self.data:
            if line.strip() == "":
                instruction_bool = True
                continue

            if instruction_bool:
                line = line.split()
                axis, flip_line = line[-1].split("=")
                self._add_to_instructions(axis, int(flip_line))
            else:
                x, y = map(int, line.split(','))
                self._add_to_points((x, y))

    def _add_to_points(self, point: Tuple[int, int], times: int = 1):
        if point not in self.points:
            self.points[point] = 0
        self.points[point] += times

    def _remove_from_points(self, point: Tuple[int, int]):
        self.points.pop(point)

    def _add_to_instructions(self, axis: str, line: int):
        self.instructions.append((axis, line))

    def _horizontal_fold(self, line: int):
        # if axis == "y"
        self.max_y = line

        to_remove: List[Tuple[int, int]] = []
        to_add: List[Tuple[Tuple[int, int], int]] = []

        for x, y in self.points:
            if y == line:
                print("Found on line: (%s, %s)" % (x, y))
            elif y > line:
                new_y = line - (y - line)

                to_remove.append((x, y))
                to_add.append(((x, new_y), self.points[(x, y)]))

        for point in to_remove:
            self._remove_from_points(point)

        for point, times in to_add:
            self._add_to_points(point, times)

    def _vertical_fold(self, line: int):
        # if axis == "x"
        self.max_x = line

        to_remove: List[Tuple[int, int]] = []
        to_add: List[Tuple[Tuple[int, int], int]] = []

        for x, y in self.points:
            if x == line:
                print("Found on line: (%s, %s)" % (x, y))
            elif x > line:
                new_x = line - (x - line)

                to_add.append(((new_x, y), self.points[(x, y)]))
                to_remove.append((x, y))

        for point in to_remove:
            self._remove_from_points(point)

        for point, times in to_add:
            self._add_to_points(point, times)

    def fold(self, instruction: Tuple[str, int]):
        axis, line = instruction

        if axis == "y":
            self._horizontal_fold(line)
        elif axis == "x":
            self._vertical_fold(line)

    def prettify(self):
        grid: List[List[str]] = []
        output = "\n"

        for _ in range(self.max_y):
            row = []
            for _ in range(self.max_x):
                row.append(" ")
            grid.append(row)

        for y, x in self.points:
            grid[x][y] = "X"

        for row in grid:
            for char in row:
                output += (char + "  ")
            output += "\n"

        return output

    def part1(self):
        self.fold(self.instructions[0])
        return len(self.points)

    def part2(self):
        for index in range(1, len(self.instructions)):
            self.fold(self.instructions[index])

        return self.prettify()


day = Day13()
day.run()
