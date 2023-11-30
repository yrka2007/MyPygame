import pygame as pg


class MainGameClass:
    def __init__(self):
        pass

    def render(self, scr: pg.Surface):
        pass

    def get_click(self, event: pg.event):
        print(event.pos)

    def get_press(self, event: pg.event):
        pass


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
                pg.draw.rect(scr, self.color, (x + col * step, y + row * step, step, step), self.board[row][col])

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



def main():
    size = width, height = 800, 600
    pg.init()
    clock = pg.time.Clock()
    fps = 50
    screen = pg.display.set_mode(size)
    objects = ()
    board = Board(16, 10)
    board.set_view(50, 20, 40)
    objects = objects + (board,)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                move_click(objects, event)
            elif event.type == pg.KEYDOWN:
                move_click(objects, event)
        screen.fill('blue')
        draw(objects, screen)
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


def move_click(obj: tuple, event: pg.event):
    for item in obj:
        item.get_click(event)


def move_press(obj: tuple, event: pg.event):
    for item in obj:
        item.get_press(event)


def draw(obj: tuple, scr: pg.Surface):
    for item in obj:
        item.render(scr)


if __name__ == '__main__':
    main()
