from typing import List
from DayBase import DayBase, DayBaseSmall


class Day10(DayBase):
    def __init__(self):
        DayBase.__init__(self, 10, to_int=False)

        self.missing_points = []

        self.matching_braces = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }

        self.illegal_lookup = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }

        self.missing_lookup = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
        }

    def parse_line(self, line: str) -> int:
        open_braces = []

        for brace in line:
            if brace in {"(", "[", "{", "<"}:
                open_braces.append(brace)
            else:
                open_brace = open_braces.pop()
                if brace != self.matching_braces[open_brace]:
                    # print("Wanted %s but found %s" % (self.matching_braces[open_brace], brace))
                    return self.illegal_lookup[brace]

        self.calculate_missing_score(open_braces)
        return 0

    def calculate_missing_score(self, stack: List[str]) -> None:
        score = 0
        while len(stack):
            open_brace = stack.pop()
            close_brace = self.matching_braces[open_brace]
            score *= 5
            score += self.missing_lookup[close_brace]
        self.missing_points.append(score)

    def part1(self):
        illegal_score = 0
        for line in self.data:
            illegal_score += self.parse_line(line)

        return illegal_score

    def part2(self):
        self.missing_points.sort()
        halfway_index = len(self.missing_points) // 2
        return self.missing_points[halfway_index]


day = Day10()
day.run()
