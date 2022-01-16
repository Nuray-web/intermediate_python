import pygame as pg
import numpy as np


class GameofLife:
    def __init__(self, surface, width=500, height=500, scale=10, offset=1, moving_cell_color=(255, 0, 0), cell_color=(255, 0, 255)):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.moving_cell_color = moving_cell_color
        self.cell_color = cell_color
        self.columns = int(height / scale)
        self.rows = int(width / scale)
        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def run(self):
        self.draw()
        self.upgrid()

    def draw(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i, j]:
                    pg.draw.rect(self.surface, self.moving_cell_color, [i * self.scale, j * self.scale, self.scale - self.offset, self.scale - self.offset])
                else:
                    pg.draw.rect(self.surface, self.cell_color, [i * self.scale, j * self.scale, self.scale - self.offset, self.scale - self.offset])



    def upgrid(self):
        updated = self.grid.copy()
        for i in range(updated.shape[0]):
            for j in range(updated.shape[1]):
                updated[i, j] = self.upcell(i, j)

        self.grid = updated


    def upcell(self, x, y):
        curr = self.grid[x, y]
        alives = 0
        for i in range(-1, 2):
            if ((x + i) < 0 or ((x + i) >= self.grid.shape[0])):
                continue
            for j in range(-1, 2):
                if ((y + j) < 0 or (y + j) >= self.grid.shape[1]):
                    continue
                if i == 0 and j == 0:
                        continue
                elif self.grid[x + i, y + j]:
                    alives += 1

        if curr and alives < 2:                                     
            return False
        elif curr and (alives == 2 or alives == 3):
            return True
        elif curr and alives > 3:                             
            return False
        elif ~curr and alives == 3:                                  
            return True
        else:
            return curr
            


screen = pg.display.set_mode((500, 500))
conway = GameofLife(screen, scale=13)

clock = pg.time.Clock()
fps = 10

while True:
    clock.tick(fps)
    screen.fill((128, 0, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    conway.run()
    pg.display.update()