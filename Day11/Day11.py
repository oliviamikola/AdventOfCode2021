from typing import List
from Octopus import Octopus
from queue import SimpleQueue
from DayBase import DayBase, DayBaseSmall


class Day11(DayBase):
    def __init__(self):
        DayBase.__init__(self, 11, to_int=False)

        self.octopi: List[List[Octopus]] = []
        for row in self.data:
            row_list = []
            for value in row:
                row_list.append(Octopus(int(value)))
            self.octopi.append(row_list)

    def pretty_print(self):
        for row in self.octopi:
            for octopus in row:
                print("%s  " % octopus.energy_level, end="")
            print()
        print()

    def _flash_neighbors(self, start_row_index: int, start_column_index: int) -> int:
        neighbors = SimpleQueue()
        neighbors.put((start_row_index, start_column_index))

        flash_count = 0

        while neighbors.qsize() != 0:
            row_index, column_index = neighbors.get()

            possible_points = []
            if row_index not in (0, 9) and column_index not in (0, 9):
                possible_points = [(row_index + x, column_index + y) for x in range(-1, 2) for y in range(-1, 2)]

            elif row_index in (0, 9) and column_index not in (0, 9):
                if row_index == 0:
                    possible_points = [(row_index + x, column_index + y) for x in range(0, 2) for y in range(-1, 2)]

                if row_index == 9:
                    possible_points = [(row_index + x, column_index + y) for x in range(-1, 1) for y in range(-1, 2)]

            elif row_index not in (0, 9) and column_index in (0, 9):
                if column_index == 0:
                    possible_points = [(row_index + x, column_index + y) for x in range(-1, 2) for y in range(0, 2)]

                if column_index == 9:
                    possible_points = [(row_index + x, column_index + y) for x in range(-1, 2) for y in range(-1, 1)]

            else:
                if row_index == 0 and column_index == 0:
                    possible_points = [(row_index + x, column_index + y) for x in range(0, 2) for y in range(0, 2)]
                elif row_index == 0 and column_index == 9:
                    possible_points = [(row_index + x, column_index + y) for x in range(0, 2) for y in range(-1, 1)]
                elif row_index == 9 and column_index == 0:
                    possible_points = [(row_index + x, column_index + y) for x in range(-1, 1) for y in range(0, 2)]
                elif row_index == 9 and column_index == 9:
                    possible_points = [(row_index + x, column_index + y) for x in range(-1, 1) for y in range(-1, 1)]

            for row, column in possible_points:
                if self.octopi[row][column].increase_level():
                    neighbors.put((row, column))
                    flash_count += 1

        return flash_count

    def complete_step(self):
        flash_count = 0
        for row_index, row in enumerate(self.octopi):
            for column_index, octopus in enumerate(row):
                if octopus.increase_level():
                    flash_count += 1

                    # flash the rest of the octopi
                    flash_count += self._flash_neighbors(row_index, column_index)

        for row in self.octopi:
            for octopus in row:
                octopus.finish_flash()
        return flash_count

    def part1(self):
        flash_count = 0
        for _ in range(100):  # 204 in 10 steps, 1656 in 100 steps
            # self.pretty_print()
            flash_count += self.complete_step()
        return flash_count

    def part2(self):
        iteration = 1
        while True:
            if self.complete_step() == 100:
                self.pretty_print()
                return iteration + 100  # the +100 is to counteract the range in part 1
            iteration += 1


day = Day11()
day.run()
