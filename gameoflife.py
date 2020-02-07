import random
import os
import time

class GameOfLife:
    row = 10
    column = 10
    board = []

    def __init__(self, rows = 10, col = 10):
        self.rows = rows
        self.column = rows
        self.board = self.create_grid()

    def create_grid(self):
        board = []
        for row in range(self.rows):
            board_row = []

        for col in range(self.rows):
            if random.randint(0,self.cols) % 2 == 0:
                board_row.append("1")
            else:
                board_row.append("0")
                
            board.append(board_row)

        return board

    def life(self,row,col):

        for row in range(self.row):
            for col in range(self.cols):
                if self.board[row][col] == '1':
                    board += '*'
                else:
                    board += ''

                    board += '\n\r'

                    print(board)

    def run(self):
        while 1:
            self.draw_board()
            self.life()
            time.sleep(0.1)




