import pygame

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [["~" for _ in range(size)] for _ in range(size)]
        self.cell_size = 40
        self.margin = 5

    def draw(self, screen, offset_x=0, offset_y=0):
        for row in range(self.size):
            for col in range(self.size):
                color = (0, 0, 255) if self.grid[row][col] == "~" else (255, 0, 0) if self.grid[row][col] == "X" else (0, 255, 0) if self.grid[row][col] == "O" else (0, 0, 0)
                pygame.draw.rect(screen,
                                 color,
                                 [(self.margin + self.cell_size) * col + self.margin + offset_x,
                                  (self.margin + self.cell_size) * row + self.margin + offset_y,
                                  self.cell_size,
                                  self.cell_size])

    def place_ship(self, ship, x, y, orientation):
        if orientation == "H":
            if y + ship.size > self.size:
                return False  # Ship can't be placed horizontally here
            for i in range(ship.size):
                self.grid[x][y + i] = ship.symbol
        else:
            if x + ship.size > self.size:
                return False  # Ship can't be placed vertically here
            for i in range(ship.size):
                self.grid[x + i][y] = ship.symbol
        return True

    def receive_attack(self, x, y):
        if self.grid[x][y] not in ["~", "X", "O"]:
            self.grid[x][y] = "X"
            return True
        elif self.grid[x][y] == "~":
            self.grid[x][y] = "O"
            return False
        return None  # Already attacked here
