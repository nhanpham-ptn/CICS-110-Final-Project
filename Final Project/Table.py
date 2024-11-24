from Checking import checking
from Sudoku_Generation import create_board


import pygame
import time

pygame.init()

white = (255,255,255)
Black = (0, 0, 0)
blue  = (0,91,150)
green = (154,224,122)
red  = (251,57,42)

window = pygame.display.set_mode((510, 600))
pygame.display.set_caption("SUDOKU")
number = pygame.font.SysFont('Arial', 30)
window.fill(white)

#drawing the board
class Board():
    def __init__(self, window):
        self.grid = create_board()
        self.window = window 
        self.selected_cell = None
    def draw_board(self):
        def create_cells():
            board = []
            for row in range(9):
                row = []
                for col in range(9):
                    cell = pygame.Rect(col * 50 + 6, row * 50 +6, 50, 50)
                    row.append(cell)
                board.append(row)
            return board 
        def draw_tiles():
            for i in range(10):
                if i % 3 ==0:
                    thickness = 6
                else:
                    thickness = 3
                pygame.draw.line(window, Black, (0, i * 50), (510, i * 50), thickness)
                pygame.draw.line(window, Black, (i * 50, 0), (i * 50, 510), thickness)
        def draw_cells(cells):
                for row in range(9):
                    for col in range(9):
                        if self.grid[row][col] != 0:
                            num = number.render(str(self.grid[row][col]), True, Black)
                            num_rect = num.get_rect(center=cells[row][col].center)
                            self.window.blit(num, num_rect)

        cells = create_cells()
        self.window.fill(white)  
        draw_tiles()
        draw_cells(cells)
        if self.selected_cell:
                (row, col) = self.selected_cell
                pygame.draw.rect(self.window, blue, cells[row][col], 5)
        
    def select(self, pos):
        (x, y) = pos
        col = int(x // 50)  
        row = int(y // 50)
        if 0 <= row <= 9 and 0 <= col <= 9:
            self.selected_cell = (row, col)
    def adding_number(self):
        



        
