import pygame

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [["~" for _ in range(size)] for _ in range(size)]
        self.cell_size = 40
        self.margin = 5
        self.width = self.size * (self.cell_size + self.margin) + self.margin
        self.height = self.size * (self.cell_size + self.margin) + self.margin
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        self.screen.fill((255, 255, 255))
        for row in range(self.size):
            for col in range(self.size):
                color = (0, 0, 255) if self.grid[row][col] == "~" else (255, 0, 0) if self.grid[row][col] == "X" else (0, 255, 0) if self.grid[row][col] == "O" else (0, 0, 0)
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.margin + self.cell_size) * col + self.margin,
                                  (self.margin + self.cell_size) * row + self.margin,
                                  self.cell_size,
                                  self.cell_size])

    def place_ship(self, ship, x, y, orientation):
        if orientation == "H":
            for i in range(ship.size):
                self.grid[x][y + i] = ship.symbol
        else:
            for i in range(ship.size):
                self.grid[x + i][y] = ship.symbol

    def receive_attack(self, x, y):
        if self.grid[x][y] != "~":
            self.grid[x][y] = "X"
            return True
        else:
            self.grid[x][y] = "O"
            return False
