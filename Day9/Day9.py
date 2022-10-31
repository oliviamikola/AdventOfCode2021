from typing import List
from queue import SimpleQueue
from DayBase import DayBase, DayBaseSmall


class Day9(DayBase):
    def __init__(self):
        DayBase.__init__(self, 9, to_int=False)
        self.basin_sizes = []

        self.heat_map: List[List[int]] = []
        for line in self.data:
            row = []
            for number in line:
                row.append(int(number))
            self.heat_map.append(row)

    def calculate_risk_level(self, low_points: List[int]):
        return sum(low_points) + len(low_points)

    def find_low_points(self):
        low_points: List[int] = []

        for row_index, row in enumerate(self.heat_map):
            for column_index, point in enumerate(row):
                # point is not in top row --> row_index == 0
                if row_index != 0 and self.heat_map[row_index - 1][column_index] <= point:
                    continue

                # point is not in bottom row --> row_index == len(self.heat_map) - 1
                if row_index != len(self.heat_map) - 1 and self.heat_map[row_index + 1][column_index] <= point:
                    continue

                # point is not in leftmost column --> column_index == 0
                if column_index != 0 and self.heat_map[row_index][column_index - 1] <= point:
                    continue

                # point is not in rightmost column --> column_index == len(row) - 1
                if column_index != len(row) - 1 and self.heat_map[row_index][column_index + 1] <= point:
                    continue

                low_points.append(point)
                self.basin_sizes.append(self.find_basin(row_index, column_index))

        return low_points

    def find_basin(self, start_row: int, start_column: int):
        basin_queue = SimpleQueue()
        basin_queue.put((start_row, start_column))
        basin_size = 0

        already_visited = set()
        
        while basin_queue.qsize() > 0:
            row, column = basin_queue.get()

            if (row, column) in already_visited:
                continue
            already_visited.add((row, column))

            point = self.heat_map[row][column]
            if point == 9:
                continue

            basin_size += 1
    
            # point is not in top row --> row == 0
            if row != 0 and self.heat_map[row - 1][column] > point:
                basin_queue.put((row - 1, column))
    
            # point is not in bottom row --> row == len(self.heat_map) - 1
            if row != len(self.heat_map) - 1 and self.heat_map[row + 1][column] > point:
                basin_queue.put((row + 1, column))
    
            # point is not in leftmost column --> column == 0
            if column != 0 and self.heat_map[row][column - 1] > point:
                basin_queue.put((row, column - 1))

            # point is not in rightmost column --> column == len(row) - 1
            if column != len(self.heat_map[0]) - 1 and self.heat_map[row][column + 1] > point:
                basin_queue.put((row, column + 1))

        return basin_size

    def part1(self):
        return self.calculate_risk_level(self.find_low_points())

    def part2(self):
        self.basin_sizes.sort(reverse=True)
        answer = 1
        for index in range(3):
            answer *= self.basin_sizes[index]
        return answer


day = Day9()
day.run()
