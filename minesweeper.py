import tkinter as tk
import random

dir = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

class Board:
    def __init__(self, width, height, num_mines):
        self.width, self.height, self.num_mines = width, height, num_mines
        self.matrix, self.shown_board = [], []
        self.win, self.lose = False, False

        for x in range(self.width):
            new = []
            blank = []
            for y in range(self.height):
                new.append(0)
                blank.append(None)
            self.matrix.append(new)
            self.shown_board.append(blank)

        self.place_mines()
        self.calc_adjacency()

    def place_mines(self):
        assert (self.num_mines >= 0 and self.num_mines <= self.width * self.height), "Invalid number of mines"

        for i in range(self.num_mines):
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            while (self.matrix[rand_x][rand_y] == -1):
                rand_x = random.randint(0, self.width - 1)
                rand_y = random.randint(0, self.height - 1)
            self.matrix[rand_x][rand_y] = 'M'

    def calc_adjacency(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.matrix[x][y] != 'M':
                    for x_dir, y_dir in dir:
                        if x + x_dir >= 0 and x + x_dir < self.width and y + y_dir >= 0 and y + y_dir < self.height:
                            if self.matrix[x + x_dir][y + y_dir] == 'M':
                                self.matrix[x][y] += 1

    #temp
    def display(self, b):
        print('   ', end = '')
        for i in range(self.height):
            print("--- ", end = '')
        print()

        for x in range(self.width):
            print("  ", end = '')
            for y in range(self.height):
                if b[x][y] == None:
                    print("|   ", end = '')
                else:
                    print("| " + str(b[x][y]) + " ", end = '')
            print("|")
            print('   ', end = '')
            for i in range(self.height):
                print("--- ", end = '')
            print()


    def open(self, x, y):
        if self.matrix[x][y] == 'M':
            self.lose = True
            return False
        self.shown_board[x][y] = self.matrix[x][y]
        if self.shown_board[x][y] == 0:
            for x_dir, y_dir in dir:
                if x + x_dir >= 0 and x + x_dir < self.width and y + y_dir >= 0 and y + y_dir < self.height:
                    if self.matrix[x + x_dir][y + y_dir] != 'M' and self.shown_board[x + x_dir][y + y_dir] == None:
                        self.open(x + x_dir, y + y_dir)
        self.check_win()

    def flag(self, x, y):
        return None

    def check_win(self):
        num_open = self.width * self.height - self.num_mines

        open = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.shown_board[x][y] != None:
                    open += 1

        if open == num_open:
            self.win = True

#beginner: 8, 8, 10
#intermediate: 16, 16, 40
#expert: 30, 16, 99

b = Board(4, 5, 3)
while(not b.lose and not b.win):
    b.display(b.matrix)
    b.display(b.shown_board)
    b.open(int(input("y: ")) - 1, int(input("x: ")) - 1)

b.display(b.matrix)
b.display(b.shown_board)
if b.lose:
    print("You lost!")
else:
    print("You won!")
