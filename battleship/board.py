import pygame

class Board:
    def __init__(self, size=10, show_ships=True):
        self.size = size
        self.grid = [["~" for _ in range(size)] for _ in range(size)]
        self.cell_size = 40
        self.margin = 5
        self.show_ships = show_ships

    def draw(self, screen, offset_x=0, offset_y=0):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.grid[row][col]
                if cell == "~":
                    color = (0, 0, 255)
                elif cell == "X":
                    color = (255, 0, 0)
                elif cell == "O":
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 0) if self.show_ships else (0, 0, 255)
                pygame.draw.rect(screen,
                                 color,
                                 [offset_x + (self.margin + self.cell_size) * col + self.margin,
                                  offset_y + (self.margin + self.cell_size) * row + self.margin,
                                  self.cell_size,
                                  self.cell_size])

    def can_place_ship(self, ship, x, y, orientation):
        if orientation == "H":
            if y + ship.size > self.size:
                return False
            for i in range(ship.size):
                if self.grid[x][y + i] != "~":
                    return False
        else:
            if x + ship.size > self.size:
                return False
            for i in range(ship.size):
                if self.grid[x + i][y] != "~":
                    return False
        return True

    def place_ship(self, ship, x, y, orientation):
        if orientation == "H":
            for i in range(ship.size):
                self.grid[x][y + i] = ship.symbol
        else:
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
