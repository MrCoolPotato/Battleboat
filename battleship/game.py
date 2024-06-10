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
            x, y = random.randint(0, board.size - 1), random.randint(0, board.size - 1)
            orientation = random.choice(["H", "V"])
            board.place_ship(ship, x, y, orientation)

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
                       
