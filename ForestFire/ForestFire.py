import sys

import pygame
import random as rd


class ForestFire:
    def __init__(self):

        pygame.init()

        self.width = 1400
        self.height = 700

        self.earth = 0
        self.tree = 1
        self.fire = 2
        self.ash = 3

        self.tree_color = (0, 255, 0)
        self.dirt_color = (220, 176, 48)
        self.fire_color = (255, 0, 0)
        self.ash_color = (90, 90, 90)

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Forest Fire")

        self.grid = self.generateLand(self.width, self.height)

    def run(self):
        clock = pygame.time.Clock()
        self.refresh()
        while True:
            self.handleInputEvents()
            clock.tick(40)
            nextStepChange = self.nextStep()

            if nextStepChange is False:
                pass
                # pygame.quit()
                # return
            else:
                self.refresh()
                pygame.display.flip()

    def generateLand(self, width, height):
        grid = []
        x = int(width / 10)
        y = int(height / 10)
        for i in range(x):
            grid.append([])
            for j in range(y):
                grid[i].append(rd.randint(0, 1))
        grid[rd.randint(0, x - 1)][rd.randint(0, y - 1)] = self.fire
        return grid

    def nextStep(self):
        newGrid = []
        x = int(self.width / 10)
        y = int(self.height / 10)
        change = False
        for i in range(x):
            newGrid.append([])
            for j in range(y):
                fire_neighbours = self.count_around_fire((i, j))
                evolve = self.evolve_cell(self.grid[i][j], fire_neighbours)
                if not change and evolve != self.grid[i][j]:
                    change = True
                newGrid[i].append(evolve)
        self.grid = newGrid
        return change

    def evolve_cell(self, status, neighbours):
        if status == self.fire:
            return self.ash
        if status == self.tree and neighbours >= 1:
            return self.fire
        return status

    def count_around_fire(self, position):
        x, y = position
        neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                           (x + 0, y - 1), (x + 0, y + 1),
                           (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
        count = 0
        for px, py in neighbour_cells:
            try:
                if self.grid[px][py] == self.fire:
                    count += 1
            except:
                pass
        return count

    def draw_block(self, x, y, color):
        block_size = 10
        x *= block_size
        y *= block_size
        center_point = ((x + (block_size / 2)), (y + (block_size / 2)))
        pygame.draw.circle(self.display, color, center_point, block_size / 2, 0)

    def refresh(self):
        for i in range(int(self.width / 10)):
            for j in range(int(self.height / 10)):
                cell = self.grid[i][j]
                cell_color = None
                if cell == self.fire:
                    cell_color = self.fire_color
                if cell == self.tree:
                    cell_color = self.tree_color
                if cell == self.ash:
                    cell_color = self.ash_color
                if cell == self.earth:
                    cell_color = self.dirt_color
                self.draw_block(i, j, cell_color)

    def handleInputEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.grid = self.generateLand(self.width, self.height)
            if event.type == pygame.KEYDOWN:
                sys.exit(0)
            if event.type == pygame.QUIT:
                print("quitting")
                sys.exit(0)
