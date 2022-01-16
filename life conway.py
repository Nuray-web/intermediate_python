import pygame as pg
import random
import time 

pg.init()

display = pg.display.set_mode((500,500), 0, 24)

def create_grid(x,y):
    grid = []
    for i in range(x):
        row = []
        for t in range(y):
            row.append(random.randint(0,1))
        grid.append(row)
    return grid

def living_cell(alive, neighbour):
    return neighbour == 3 or (neighbour == 2 and alive)

def count(grid, pos):
    x, y = pos
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x>= 0 and y>= 0:
            try:
                count += grid[x][y]
            except:
                pass 
    return count                        

def dev(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = create_grid(x, y)
    for i in range(x):
        for t in range(y):
            cell = grid[i][t]
            neighbour = count(grid, (i, t))
            if living_cell(cell, neighbour):
                new_grid[i][t] = 1
            else:
                new_grid[i][t] = 0
    return new_grid

def update(x, y, color):
    cell_size = 10
    x *= cell_size
    y *= cell_size
    center = ((x + (cell_size/2))), ((y + (cell_size/2)))
    pg.draw.circle(display, color, center, cell_size/2)

def main():
    n = 0
    cell_count = 0
    alive_cell_color = pg.Color(0,0,0)
    alive_cell_color.hsva = [n, 100, 100]
    xlen = 50
    ylen = 50
    while True:
        space = create_grid(xlen, ylen)
        for i in range(200):
            for x in range(xlen):
                for y in range(ylen):
                    alive = space[x][y]
                    cell_count += 1
                    if alive:
                        cell_color = alive_cell_color
                    else:
                        cell_color = (0,0,0)
                    update(x, y, cell_color)
            pg.display.flip()
            n = (n+2) % 360
            alive_cell_color.hsva = (n, 100, 100)
            space = dev(space)
            cell_count = 0
            time.sleep(0.1)

if __name__ == '__main__':
    main()