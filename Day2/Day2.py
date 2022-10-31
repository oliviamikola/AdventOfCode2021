from DayBase import DayBase


class Day2(DayBase):
    def __init__(self):
        DayBase.__init__(self, 2, to_int=False)

        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def _clear(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def _parse(self, direction: str, amount: int):
        if direction == "forward":
            self.horizontal += amount
        elif direction == "up":
            self.depth -= amount
        elif direction == "down":
            self.depth += amount
        else:
            print("Bad direction: %s" % direction)

    def _parse2(self, direction: str, amount: int):
        if direction == "forward":
            self.horizontal += amount
            self.depth += (self.aim * amount)
        elif direction == "up":
            self.aim -= amount
        elif direction == "down":
            self.aim += amount
        else:
            print("Bad direction: %s" % direction)

    def part1(self):
        self._clear()
        for line in self.data:
            direction, amount = line.split()
            self._parse(direction, int(amount))

        return self.horizontal * self.depth

    def part2(self):
        self._clear()
        for line in self.data:
            direction, amount = line.split()
            self._parse2(direction, int(amount))

        return self.horizontal * self.depth


day = Day2()
day.run()
