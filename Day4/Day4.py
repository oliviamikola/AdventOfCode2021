from typing import List, Optional
from DayBase import DayBase, DayBaseSmall
from Board import Board


class Day4(DayBase):
    def __init__(self):
        DayBase.__init__(self, 4, to_int=False)

        self.called_numbers = list(map(int, self.data[0].split(",")))

        self.board_list = []
        for board_number in range((len(self.data) - 1) // 6):
            start_row_index = 2 + board_number * 6
            self.board_list.append(Board(self.data[start_row_index: start_row_index + 5]))

    def _check_for_final_board(self) -> bool:
        for board in self.board_list:
            if not board.win:
                return False
        return True

    def play_bingo(self):
        for number in self.called_numbers:
            for board in self.board_list:
                board.mark_number(number)
                if board.check_board_for_win():
                    return board.calculate_score(number)

    def let_squid_win(self):
        for number in self.called_numbers:
            for board in self.board_list:
                board.mark_number(number)
                if board.check_board_for_win():
                    board.win = True
                    if self._check_for_final_board():
                        return board.calculate_score(number)

    def part1(self):
        return self.play_bingo()

    def part2(self):
        return self.let_squid_win()


day = Day4()
day.run()
