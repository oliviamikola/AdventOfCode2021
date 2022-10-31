from typing import Dict
from DayBase import DayBase, DayBaseSmall


class Day14(DayBase):
    def __init__(self):
        DayBase.__init__(self, 14, to_int=False)

        self.code = ""

        self.code_count: Dict[str, int] = {}
        self.char_count: Dict[str, int] = {}

        self.matchup: Dict[str, str] = {}

        for index, line in enumerate(self.data):
            if index == 0:
                self.code = line
                continue
            if index == 1:
                continue

            key, value = line.split(" -> ")
            self.matchup[key] = value
            self.code_count[key] = 0
            self.char_count[value] = 0

        for index in range(1, len(self.code)):
            sub_code = self.code[index - 1: index + 1]
            self.code_count[sub_code] += 1

        for char in self.code:
            self.char_count[char] += 1

    def parse(self):
        new_code_count = {key: 0 for key in self.code_count}

        for pattern, count in self.code_count.items():
            if count == 0:
                continue

            result = self.matchup[pattern]
            self.char_count[result] += count

            p1 = pattern[0] + result
            p2 = result + pattern[1]

            new_code_count[p1] += count
            new_code_count[p2] += count

        self.code_count = new_code_count

    def count(self):
        count_list = sorted(v for v in self.char_count.values())
        return count_list[-1] - count_list[0]

    def part1(self):
        for _ in range(10):
            self.parse()

        return self.count()

    def part2(self):
        for _ in range(30):  # Offsets the 10 iterations already performed in part 1
            self.parse()

        return self.count()


day = Day14()
day.run()
