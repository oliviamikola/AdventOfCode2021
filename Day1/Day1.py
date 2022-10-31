from DayBase import DayBase


class Day1(DayBase):
    def __init__(self):
        DayBase.__init__(self, 1, to_int=True)

    def part1(self):
        greater_counter: int = 0

        for index in range(1, len(self.data)):
            if self.data[index] > self.data[index - 1]:
                greater_counter += 1

        return greater_counter

    def part2(self):
        greater_count: int = 0

        for index in range(3, len(self.data)):
            if self.data[index] > self.data[index - 3]:
                greater_count += 1

        return greater_count


day = Day1()
day.run()

