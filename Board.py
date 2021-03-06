# File that holds the Sudoku boards


class Board:
    def __init__(self):
        self.board = []

    def set_board(self, board_num):
        if board_num == 1:
            self.board = [[7,8,0,4,0,0,1,2,0],
                            [6,0,0,0,7,5,0,0,9],
                            [0,0,0,6,0,1,0,7,8],
                            [0,0,7,0,4,0,2,6,0],
                            [0,0,1,0,5,0,9,3,0],
                            [9,0,4,0,6,0,0,0,5],
                            [0,7,0,3,0,0,0,1,2],
                            [1,2,0,0,0,7,4,0,0],
                            [0,4,9,2,0,6,0,0,7]]
        elif board_num == 2:
            self.board = [[0,8,0,4,0,9,0,5,0],
                            [5,0,2,0,0,6,0,0,3],
                            [4,0,0,0,0,7,0,1,0],
                            [3,0,0,0,0,2,0,7,0],
                            [7,0,0,3,0,8,0,0,1],
                            [0,4,0,6,0,0,0,0,8],
                            [0,1,0,5,0,0,0,0,9],
                            [2,0,0,7,0,0,6,0,5],
                            [0,5,0,9,0,4,0,8,0]]
        elif board_num == 3:
            self.board = [[7,0,3,0,0,0,0,0,6],
                            [0,1,0,0,0,9,0,0,0],
                            [0,9,6,1,0,0,0,3,0],
                            [5,0,0,0,0,7,9,0,4],
                            [0,0,0,8,1,0,2,0,0],
                            [0,0,0,5,0,0,0,0,0],
                            [0,0,2,4,0,0,0,0,8],
                            [0,0,0,0,0,0,0,0,0],
                            [3,0,4,0,0,0,0,6,0]]

    def get_board(self):
        return self.board
