from typing import List

class Solution:
    def __init__(self):
        self.state = []

    def to_type(self, t, _board):
        for line in range(len(_board)):
            for cell in range(9):
                _board[line][cell] = t(_board[line][cell]) if t is str or _board[line][cell].isdigit() else None

    @staticmethod
    def get_square_coordinates(line, cell):
        start_line, start_cell = line - line % 3, cell - cell % 3
        end_cell = start_cell + 2
        for _ in range(9):
            if start_cell > end_cell:
                start_cell -= 3
                start_line += 1
            yield [start_line, start_cell]
            start_cell += 1

    @staticmethod
    def rollback_board(state, _board):
        for coord in state:
            _board[coord[0]][coord[1]] = None
        del state

    def get_available_values(self, line: int, cell: int, _board: List[List[str]]):
        nums = set(range(1, 10))
        cell_values = {_board[_line][cell] for _line in range(9)}
        square_values = {_board[c[0]][c[1]] for c in self.get_square_coordinates(line, cell)}
        return (nums ^ (set(_board[line]) | cell_values | square_values)) ^ {None}

    @staticmethod
    def check_solved(_board):
        return all(all(line) for line in _board)

    def fill_cells(self, board, choices=1):
        if choices == 1:
            self.state.append([])
        # run until board is filled
        while True:

            filled = False
            # loop through all cells
            for i in range(81):
                cell = i % 9
                line = int(i / 9)
                if not board[line][cell]:
                    values = self.get_available_values(line, cell, board)
                    if not len(values):
                        self.rollback_board(self.state.pop(), board)
                        return False
                    # we start looking from choices=1 to fill all data we can
                    # after we increase `choices` to check which value fits better
                    if len(values) == choices:
                        # flag to see where to stop implicit loop
                        fit = False

                        self.state[-1].append([line, cell])
                        # loop through all available values

                        while values and not fit:
                            board[line][cell] = values.pop()
                            # recursively call `fill_cell` if we test values.
                            # Rollback if puzzle cannot be solved with this value
                            filled = fit = self.fill_cells(board) if choices > 1 else True
            if self.check_solved(board):
                return True
            elif filled:
                continue
            else:
                # increase available choices to check for cell values
                return self.fill_cells(board, choices + 1)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.to_type(int, board)
        self.fill_cells(board)
        self.to_type(str, board)

