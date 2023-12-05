from copy import deepcopy
import pygame as pg
from gamebase import MainGameClass


class Board(MainGameClass):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = "gray"

    def set_view(self, left, top, cell_size, color="gray"):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = color

    def render(self, scr: pg.Surface, state):
        x = self.left
        y = self.top
        step = self.cell_size
        for row in range(self.height):
            for col in range(self.width):
                if state:
                    pg.draw.circle(scr, 'white', (x + col * step + step // 2, y + row * step + step), step // 2)
                else:
                    pg.draw.circle(scr, 'gray', (x + col * step + step // 2, y + row * step + step), step // 2)
                if self.board[row][col]:
                    pg.draw.circle(scr, 'red', (x + col * step + step // 2, y + row * step + step), step // 2 - 6)

                # pg.draw.rect(scr, self.color, (x + col * step, y + row * step, step, step), self.board[row][col])

    def get_click(self, event: pg.event):
        coord = self.get_cell(event.pos)
        if coord:
            col = coord[0]
            row = coord[1]
            self.board[row][col] = (self.board[row][col] + 1) % 2

    def get_cell(self, mouse_pos: tuple):
        x0 = mouse_pos[0] - self.left
        y0 = mouse_pos[1] - self.top
        col = x0 // self.cell_size
        row = y0 // self.cell_size
        if 0 <= col < self.width and 0 <= row < self.height:
            return col, row
        else:
            return None

    def next_move(self):
        tboard = deepcopy(self.board)
        for row in range(self.height):
            for col in range(self.width):
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if not (x == 0 and y == 0):
                            count += self.get_state(tboard, col + x, row + y)
                if count == 3:
                    self.board[row][col] = 1
                elif count == 2 and self.board[row][col] == 1:
                    self.board[row][col] = 1
                else:
                    self.board[row][col] = 0

    def get_state(self, tboard, col, row):
        if col < 0:
            col = self.width + col
        elif col >= self.width:
            col = col - self.width
        if row < 0:
            row = self.height + row
        elif row >= self.height:
            row = row - self.height
        return tboard[row][col]


class Life(Board):
    pass
