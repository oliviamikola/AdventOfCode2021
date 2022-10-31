from typing import List


class Board:
    def __init__(self, board: List[List[str]]):
        self.win = False
        self.board = []
        for row in board:
            self.board.append(list(map(int, row.split())))

        self.marked_board = [[False for _ in range(5)] for _ in range(5)]

    def pretty_print(self):
        for row in self.board:
            for spot in row:
                print("%s  " % spot, end="")
            print()
        print()

    def reset_board(self):
        self.marked_board = [[False for _ in range(5)] for _ in range(5)]
        self.win = False

    def mark_number(self, called: int) -> None:
        for row_index in range(5):
            for column_index in range(5):
                if self.board[row_index][column_index] == called:
                    self.marked_board[row_index][column_index] = True
                    break

    def check_board_for_win(self) -> bool:
        for row in self.marked_board:
            if all(row):
                return True

        for column_index in range(5):
            if all(self.marked_board[row_index][column_index] for row_index in range(5)):
                return True

        return False

    def calculate_score(self, called: int):
        total = 0
        for row_index in range(5):
            for column_index in range(5):
                if not self.marked_board[row_index][column_index]:
                    total += self.board[row_index][column_index]
        return total * called
