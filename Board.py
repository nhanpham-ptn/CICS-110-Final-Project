from Checking import is_valid_move
from Sudoku_Generation import create_board
import random


import pygame
import time

pygame.init()

# Get some colors for the GUI
white = (255,255,255)
Black = (0, 0, 0)
blue  = (0,91,150)
green = (154,224,122)
red  = (251,57,42)

window = pygame.display.set_mode((510, 600))
pygame.display.set_caption("SUDOKU")
number = pygame.font.SysFont('Arial', 30)
window.fill(white)





# defining the board object
class Board:
    def __init__(self, window, difficulty):
        self.window = window
        self.difficulty = difficulty
        self.board = create_board()
        self.grid = self.make_puzzle(self.board, difficulty)
        self.attempt = 3
        self.selected_cell = None

    
    def make_puzzle(self, board, difficulty):
        import copy
        puzzle = copy.deepcopy(board)
        
        if difficulty == 'easy':
            cells_to_remove = 30
        elif difficulty == 'medium':
            cells_to_remove = 45
        elif difficulty == 'hard':
            cells_to_remove = 55
        else:
            cells_to_remove = 30

        while cells_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                cells_to_remove -= 1

        return puzzle

    def draw_board(self):
        def create_cells():
            board = []
            for row in range(9):
                rows = []
                for col in range(9):
                    cell = pygame.Rect(col * (510/9), row * (510/9), (510/9), (510/9))
                    rows.append(cell)
                board.append(rows)
            return board 
        def draw_lines():
            for i in range(10):
                if i % 3 ==0:
                    thickness = 6
                else:
                    thickness = 3
                pygame.draw.line(window, Black, (0, i * (510/9)), (510, i * (510/9)), thickness)
                pygame.draw.line(window, Black, (i * (510/9), 0), (i * (510/9), 510), thickness)
        def draw_cells(cells):
                for row in range(9):
                    for col in range(9):
                        if self.grid[row][col] != 0:
                            num = number.render(str(self.grid[row][col]), True, Black)
                            num_rect = num.get_rect(center=cells[row][col].center)
                            self.window.blit(num, num_rect)

        cells = create_cells()
        self.window.fill(white)  
        draw_lines()
        draw_cells(cells)
        if self.selected_cell:
                (row, col) = self.selected_cell
                pygame.draw.rect(self.window, blue, cells[row][col], 5)
        font = pygame.font.SysFont('Arial', 30)
        attempts = font.render(f" Strikes left: {self.attempt} ", True, Black)
        attempt_rec = attempts.get_rect(center=(80, 550))
        pygame.draw.rect(self.window, Black, attempt_rec ,width=2, border_radius=0)
        window.blit(attempts, attempt_rec)
    def select(self, pos):
        (x, y) = pos
        col = int(x // (510/9))  
        row = int(y // (510/9))
        if 0 <= row <= 9 and 0 <= col <= 9:
            self.selected_cell = (row, col)
        return self.selected_cell 
    def adding_number(self, num):
        (row, col) = self.selected_cell
        if not self.grid[row][col] == 0:
            pass
        else:
            self.grid[row][col] = num
            return True
        return False
    def deselect(self):
        self.selected_cell = None
    
    def correct(self, num):
        if not self.selected_cell:
            return False

        (row, col) = self.selected_cell

        if self.grid[row][col] == 0:
            if is_valid_move(self.grid, row, col, num):
                self.grid[row][col] = num
                cell = pygame.Rect(col * (510 / 9), row * (510 / 9), (510 / 9), (510 / 9))
                pygame.draw.rect(self.window, green, cell, 5)
                pygame.display.update()
                pygame.time.delay(300)
                return True
            else:
                cell = pygame.Rect(col * (510 / 9), row * (510 / 9), (510 / 9), (510 / 9))
                pygame.draw.rect(self.window, red, cell, 5)
                self.attempt -= 1
                pygame.display.update()
                pygame.time.delay(300)
                return False

        return False

    def end(self):
        result = False
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    result = True
                
        return result