import pygame
from battleship.board import Board
from battleship.ship import ships
import random

class Game:
    def __init__(self, show_enemy_ships=True):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 600))  
        pygame.display.set_caption("Battleship Game")
        self.player_board = Board()
        self.ai_board = Board(show_ships=show_enemy_ships)
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
                if board.can_place_ship(ship, x, y, orientation):
                    board.place_ship(ship, x, y, orientation)
                    placed = True

    def play(self):
        running = True
        player_turn = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                    x, y = pygame.mouse.get_pos()
                    board_x_start = 550
                    board_y_start = 100
                    cell_size_with_margin = self.ai_board.cell_size + self.ai_board.margin
                    board_x_end = board_x_start + self.ai_board.size * cell_size_with_margin
                    board_y_end = board_y_start + self.ai_board.size * cell_size_with_margin
                    if board_x_start <= x < board_x_end and board_y_start <= y < board_y_end: 
                        col = (x - board_x_start) // cell_size_with_margin
                        row = (y - board_y_start) // cell_size_with_margin
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
            if any(cell in ["R", "S", "C"] for cell in row):  
                return False
        return True

    def draw_boards(self):
       
        self.player_board.draw(self.screen, offset_x=50, offset_y=100)
        player_label = self.font.render("Player Board", True, (0, 0, 0))
        self.screen.blit(player_label, (50, 50))

        
        self.ai_board.draw(self.screen, offset_x=550, offset_y=100)
        ai_label = self.font.render("AI Board", True, (0, 0, 0))
        self.screen.blit(ai_label, (550, 50))
