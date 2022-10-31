from typing import Dict, Set, Tuple, List
from DayBase import DayBase, DayBaseSmall


class Day8(DayBase):
    def __init__(self):
        DayBase.__init__(self, 8, to_int=False)

        self.digit_map: Dict[int, Set[str]] = {
            0: {"a", "b", "c", "e", "f", "g"},
            1: {"c", "f"},
            2: {"a", "c", "d", "e", "g"},
            3: {"a", "c", "d", "f", "g"},
            4: {"b", "c", "d", "f"},
            5: {"a", "b", "d", "f", "g"},
            6: {"a", "b", "d", "e", "f", "g"},
            7: {"a", "c", "f"},
            8: {"a", "b", "c", "d", "e", "f", "g"},
            9: {"a", "b", "c", "d", "f", "g"}
        }

        self.lengths: Dict[int, Tuple[int]] = {
            2: (1,),
            3: (7,),
            4: (4,),
            5: (2, 3, 5),
            6: (0, 6, 9),
            7: (8,)
        }

        self.found_digits: Dict[int, int] = {i: 0 for i in range(10)}

    def count_number_of_digits(self) -> int:
        found_digits = 0
        for line in self.data:
            input_string, output_string = line.split(" | ")
            inputs, outputs = sorted(input_string.split(), key=len), sorted(output_string.split(), key=len)

            for output in outputs:
                if len(output) == len(self.digit_map[1]):
                    found_digits += 1
                elif len(output) == len(self.digit_map[4]):
                    found_digits += 1
                elif len(output) == len(self.digit_map[7]):
                    found_digits += 1
                elif len(output) == len(self.digit_map[8]):
                    found_digits += 1

        return found_digits

    def solve_line(self, line: str):
        # Key = how the signal is presenting itself, Value = what belongs in the digit map
        line_digit_map: Dict[str, str] = {}

        input_string, output_string = line.split(" | ")
        inputs, o = sorted(input_string.split(), key=len), output_string.split()

        outputs = []
        for output in o:
            outputs.append(frozenset(output))

        candidates = [[] for _ in range(10)]
        for inpt in inputs:
            for length in self.lengths[len(inpt)]:
                candidates[length].append(frozenset(inpt))

        d1 = candidates[1][0]
        d4 = candidates[4][0]

        # 2, 5, and 6 must not contain both segments of 1.
        for i in (2, 5, 6):
            candidates[i] = [c for c in candidates[i] if not d1.issubset(c)]

        # The intersection of 5 and 4 must have length 3.
        candidates[5] = [c for c in candidates[5] if len(d4.intersection(c)) == 3]

        # The intersection of 2 and 4 must have length 2.
        candidates[2] = [c for c in candidates[2] if len(d4.intersection(c)) == 2]

        # The intersection of 9 and 4 must have length 4.
        candidates[9] = [c for c in candidates[9] if len(d4.intersection(c)) == 4]

        # The intersection of 3 and 1 must have length 2.
        candidates[3] = [c for c in candidates[3] if len(d1.intersection(c)) == 2]

        # The intersection of 0 and 1 must have length 2 and between 0 and 4 is must have length 3.
        candidates[0] = [c for c in candidates[0]
                         if len(d1.intersection(c)) == 2 and len(d4.intersection(c)) == 3]

        pattern = {c[0]: i for i, c in enumerate(candidates)}

        number = 0
        for i, magnitude in enumerate((1000, 100, 10, 1)):
            number += pattern[outputs[i]] * magnitude

        return number

    def part1(self):
        return self.count_number_of_digits()

    def part2(self):
        result = 0
        for line in self.data:
            result += self.solve_line(line)
        return result


day = Day8()
day.run()
