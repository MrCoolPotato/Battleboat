import pygame
from battleship.board import Board
from battleship.ship import ships
import random

class Game:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.ships = ships
        self.ai_board = Board()
        self.ai_ships = ships

    def start(self):
        self.setup_board(self.board, self.ships)
        self.setup_board(self.ai_board, self.ai_ships)
        self.play()

    def setup_board(self, board, ships):
        for ship in ships:
            placed = False
            while not placed:
                x, y = random.randint(0, board.size - 1), random.randint(0, board.size - 1)
                orientation = random.choice(["H", "V"])
                placed = board.place_ship(ship, x, y, orientation)

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = y // (self.board.cell_size + self.board.margin)
                    col = x // (self.board.cell_size + self.board.margin)
                    if row < self.board.size and col < self.board.size:
                        if self.ai_board.receive_attack(row, col):
                            print("Hit!")
                        else:
                            print("Miss!")
                        if self.check_winner(self.ai_board):
                            print("You win!")
                            running = False
                            
                        x, y = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
                        if self.board.receive_attack(x, y):
                            print("AI hit your ship!")
                        else:
                            print("AI missed!")

                        if self.check_winner(self.board):
                            print("AI wins!")
                            running = False

            self.board.draw()
            pygame.display.flip()

        pygame.quit()

    def check_winner(self, board):
        for row in board.grid:
            if any(cell in ["R", "S"] for cell in row):
                return False
        return True
