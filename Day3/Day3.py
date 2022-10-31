from typing import List

from DayBase import DayBase


class Day3(DayBase):
    def __init__(self):
        DayBase.__init__(self, 3, to_int=False)

        self.gamma_rate: str = ""
        self.epsilon_rate: str = ""
        self.oxygen_rating: str = ""
        self.co2_rating: str = ""

        self._find_all_rates()

    def _find_all_rates(self) -> None:
        self._find_gamma_rate()
        self._find_epsilon_rate()
        self._find_oxygen_rating()
        self._find_co2_rating()

    def _calculate_consumption_rate(self) -> int:
        return int(self.gamma_rate, 2) * int(self.epsilon_rate, 2)

    def _calculate_oxygen_generator_rate(self) -> int:
        return int(self.oxygen_rating, 2) * int(self.co2_rating, 2)

    def _find_gamma_rate(self):
        one_bit_counter: dict[int, int] = {}
        total_numbers = 0
        number_length = 0

        for number in self.data:
            total_numbers += 1
            if len(one_bit_counter) == 0:
                number_length = len(number)
                for key in range(number_length):
                    one_bit_counter[key] = 0

            for bit_key, bit in enumerate(number):
                one_bit_counter[bit_key] += int(bit)

        for bit_key in range(number_length):
            if one_bit_counter[bit_key] / total_numbers >= 0.5:
                self.gamma_rate += "1"
            else:
                self.gamma_rate += "0"

    def _find_epsilon_rate(self):
        for bit in self.gamma_rate:
            if bit == "1":
                self.epsilon_rate += "0"
            elif bit == "0":
                self.epsilon_rate += "1"

    def _find_oxygen_rating(self):
        current_allowed_data = self.data.copy()
        allowed_data = []

        for bit_index in range(len(self.gamma_rate)):
            if len(current_allowed_data) == 1:
                break

            most_common_bit = Day3._find_most_common(current_allowed_data, bit_index)

            for number in current_allowed_data:
                if number[bit_index] == most_common_bit:
                    allowed_data.append(number)

            current_allowed_data = allowed_data.copy()
            allowed_data.clear()

        self.oxygen_rating = current_allowed_data[0]

    def _find_co2_rating(self):
        current_allowed_data = self.data.copy()
        allowed_data = []

        for bit_index in range(len(self.gamma_rate)):
            if len(current_allowed_data) == 1:
                break

            least_common_bit = Day3._find_least_common(current_allowed_data, bit_index)

            for number in current_allowed_data:
                if number[bit_index] == least_common_bit:
                    allowed_data.append(number)

            current_allowed_data = allowed_data.copy()
            allowed_data.clear()

        self.co2_rating = current_allowed_data[0]

    @staticmethod
    def _find_most_common(bit_list: List[str], bit_position: int) -> str:
        one_bit_count = 0

        for number in bit_list:
            one_bit_count += int(number[bit_position])

        if one_bit_count / len(bit_list) >= 0.5:
            return "1"
        return "0"

    @staticmethod
    def _find_least_common(bit_list: List[str], bit_position: int) -> str:
        one_bit_count = 0

        for number in bit_list:
            one_bit_count += int(number[bit_position])

        if one_bit_count / len(bit_list) < 0.5:
            return "1"
        return "0"

    def part1(self):
        return self._calculate_consumption_rate()

    def part2(self):
        return self._calculate_oxygen_generator_rate()


day = Day3()
day.run()
