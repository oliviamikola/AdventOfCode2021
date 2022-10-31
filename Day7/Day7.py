import sys
from DayBase import DayBase, DayBaseSmall


class Day7(DayBase):
    def __init__(self):
        DayBase.__init__(self, 7, to_int=False)

        self.crab_positions = list(map(int, self.data[0].split(",")))

    def _calculate_total_fuel_cost(self, position: int) -> int:
        total_fuel_cost = 0

        for crab in self.crab_positions:
            total_fuel_cost += abs(crab - position)

        return total_fuel_cost

    def _calculate_total_expensive_fuel_cost(self, position: int) -> int:
        total_fuel_cost = 0

        for crab in self.crab_positions:
            distance = abs(crab - position)
            total_fuel_cost += ((distance * (distance + 1)) // 2)

        return total_fuel_cost

    def calculate_best_position(self, expensive_fuel=False) -> int:
        max_position, min_position = max(self.crab_positions), min(self.crab_positions)

        lowest_fuel_cost = sys.maxsize
        for position in range(min_position, max_position + 1):
            if expensive_fuel:
                position_fuel_cost = self._calculate_total_expensive_fuel_cost(position)
            else:
                position_fuel_cost = self._calculate_total_fuel_cost(position)

            if position_fuel_cost < lowest_fuel_cost:
                lowest_fuel_cost = position_fuel_cost

        return lowest_fuel_cost

    def part1(self):
        return self.calculate_best_position()

    def part2(self):
        return self.calculate_best_position(expensive_fuel=True)


day = Day7()
day.run()
