import pygame as pg
from gamebase import MainGameClass


class Board(MainGameClass):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = "gray"

    def set_view(self, left, top, cell_size, color="gray"):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = color

    def render(self, scr: pg.Surface):
        x = self.left
        y = self.top
        step = self.cell_size
        for row in range(self.height):
            for col in range(self.width):
                pg.draw.circle(scr, 'white', (x + col * step + step // 2, y + row * step + step), step // 2)
                if self.board[row][col]:
                    pg.draw.circle(scr, 'red', (x + col * step + step // 2, y + row * step + step), step // 2 - 6)

                # pg.draw.rect(scr, self.color, (x + col * step, y + row * step, step, step), self.board[row][col])

    def get_click(self, event: pg.event):
        coord = self.get_cell(event.pos)
        if coord:
            col = coord[0]
            row = coord[1]
            for c in range(self.width):
                self.board[row][c] = (self.board[row][c] + 1) % 2
            for r in range(self.height):
                if r != row:
                    self.board[r][col] = (self.board[r][col] + 1) % 2

    def get_cell(self, mouse_pos: tuple):
        x0 = mouse_pos[0] - self.left
        y0 = mouse_pos[1] - self.top
        col = x0 // self.cell_size
        row = y0 // self.cell_size
        if 0 <= col < self.width and 0 <= row < self.height:
            return col, row
        else:
            return None
