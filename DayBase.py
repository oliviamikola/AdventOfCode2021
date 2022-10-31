import time
from collections.abc import Callable
from typing import List, TypeVar


class DayBase:
    def __init__(self, number: int, to_int: bool = False):
        self.fileName: str = "Day%sData.txt" % number
        # self.data: List[str] = open(self.fileName, "r").read().splitlines()

        if to_int:
            self.data = list(map(int, open(self.fileName).read().splitlines()))
        else:
            self.data = open(self.fileName).read().splitlines()

    def part1(self):
        pass

    def part2(self):
        pass

    def run(self):
        def _run():
            print("Result of Part 1: %s" % self.part1())
            print("Result of Part 2: %s" % self.part2())

        start_time = time.time_ns()
        _run()
        end_time = time.time_ns()

        total_time = (end_time - start_time)

        print("Project Runtime: %sns" % total_time)


class DayBaseSmall:
    def __init__(self, number: int, to_int: bool = False):
        self.fileName: str = "Day%sSmallData.txt" % number
        # self.data: List[str] = open(self.fileName, "r").read().splitlines()

        if to_int:
            self.data = list(map(int, open(self.fileName).read().splitlines()))
        else:
            self.data = open(self.fileName).read().splitlines()

    def part1(self):
        pass

    def part2(self):
        pass

    def run(self):
        def _run():
            print("Result of Part 1: %s" % self.part1())
            print("Result of Part 2: %s" % self.part2())

        start_time = time.time_ns()
        _run()
        end_time = time.time_ns()

        total_time = (end_time - start_time)

        print("Project Runtime: %sns" % total_time)
