from DayBase import DayBase, DayBaseSmall


class Day6(DayBase):
    def __init__(self):
        DayBase.__init__(self, 6, to_int=False)

        self.fish_states = list(map(int, self.data[0].split(",")))

        self.fish_state_counter = {}
        self._initialize_fish_state_counter()

    def _initialize_fish_state_counter(self):
        self.fish_state_counter = {}
        for i in range(9):
            self.fish_state_counter[i] = 0

        for state in self.fish_states:
            self.fish_state_counter[state] += 1

    def _count_fish(self) -> int:
        total_fish = 0

        for state in self.fish_state_counter:
            total_fish += self.fish_state_counter[state]

        return total_fish

    def _calculate_fish_population(self, days: int) -> int:
        self._initialize_fish_state_counter()
        for _ in range(days):
            new_fish_count = self.fish_state_counter[0]
            for state in range(1, 9):
                self.fish_state_counter[state - 1] = self.fish_state_counter[state]

            self.fish_state_counter[8] = new_fish_count
            self.fish_state_counter[6] += new_fish_count

        return self._count_fish()

    def part1(self):
        return self._calculate_fish_population(80)

    def part2(self):
        return self._calculate_fish_population(256)


day = Day6()
day.run()
