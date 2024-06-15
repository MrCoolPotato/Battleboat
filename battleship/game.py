import pygame
from battleship.board import Board
from battleship.ship import ships
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Battleship Game")
        self.player_board = Board()
        self.ai_board = Board()
        self.ships = ships
        self.ai_ships = ships
        self.ai_hits = []
        self.font = pygame.font.SysFont(None, 36)

    def start(self):
        self.setup_board(self.player_board, self.ships)
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
        player_turn = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                    x, y = pygame.mouse.get_pos()
                    if 500 <= x <= 500 + self.ai_board.size * (self.ai_board.cell_size + self.ai_board.margin) and 100 <= y <= 100 + self.ai_board.size * (self.ai_board.cell_size + self.ai_board.margin): 
                        col = (x - 500) // (self.ai_board.cell_size + self.ai_board.margin)
                        row = (y - 100) // (self.ai_board.cell_size + self.ai_board.margin)
                        if 0 <= row < self.ai_board.size and 0 <= col < self.ai_board.size:
                            result = self.ai_board.receive_attack(row, col)
                            if result is not None:
                                player_turn = False
                                if result:
                                    print("Hit!")
                                else:
                                    print("Miss!")
                                if self.check_winner(self.ai_board):
                                    print("You win!")
                                    running = False

            if not player_turn:
                self.ai_turn()
                player_turn = True

            self.screen.fill((255, 255, 255))
            self.draw_boards()
            pygame.display.flip()

        pygame.quit()

    def ai_turn(self):
        if self.ai_hits:
            last_hit = self.ai_hits[-1]
            potential_moves = self.get_potential_moves(last_hit)
            for move in potential_moves:
                if 0 <= move[0] < self.player_board.size and 0 <= move[1] < self.player_board.size:
                    result = self.player_board.receive_attack(move[0], move[1])
                    if result is not None:
                        if result:
                            self.ai_hits.append(move)
                            print("AI hit your ship!")
                            if self.check_winner(self.player_board):
                                print("AI wins!")
                                pygame.quit()
                        else:
                            print("AI missed!")
                        return

        while True:
            x, y = random.randint(0, self.player_board.size - 1), random.randint(0, self.player_board.size - 1)
            result = self.player_board.receive_attack(x, y)
            if result is not None:
                if result:
                    self.ai_hits.append((x, y))
                    print("AI hit your ship!")
                    if self.check_winner(self.player_board):
                        print("AI wins!")
                        pygame.quit()
                else:
                    print("AI missed!")
                break

    def get_potential_moves(self, last_hit):
        x, y = last_hit
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def check_winner(self, board):
        for row in board.grid:
            if any(cell in ["R", "S"] for cell in row):
                return False
        return True

    def draw_boards(self):
        
        self.player_board.draw(self.screen, offset_x=50, offset_y=100)
        player_label = self.font.render("Player Board", True, (0, 0, 0))
        self.screen.blit(player_label, (50, 50))

        
        self.ai_board.draw(self.screen, offset_x=500, offset_y=100)
        ai_label = self.font.render("AI Board", True, (0, 0, 0))
        self.screen.blit(ai_label, (500, 50))
