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
        self.attempt = 3
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
        if self.adding_number(num):
            (row, col) = self.selected_cell
            cell = pygame.Rect(col * (510/9), row * (510/9), (510/9), (510/9))
            if checking(self.grid, num , row, col):
                pygame.draw.rect(self.window, green, cell, 5)
                self.grid[row][col] = num
                pygame.display.update()
                pygame.time.delay(1000)
                return True
            else:
                pygame.draw.rect(self.window, red, cell, 5)
                self.grid[row][col] = 0 
                pygame.display.update()
                pygame.time.delay(1000)
                return False


    def get_attempt(self):
        return self.attempt



def play_game():
        grid = Board(window)
        selected_cell = None
        run = True


        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    grid.draw_board()
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] < 510 and pos[1] < 510:
                            selected_cell = grid.select(pos)
                            (row, col) = selected_cell
                elif event.type == pygame.KEYDOWN and selected_cell:
                    if event.key == pygame.K_1:
                         grid.correct(1)
                    elif event.key == pygame.K_2:
                         grid.correct(2)
                    elif event.key == pygame.K_3:
                         grid.correct(3)
                    elif event.key == pygame.K_4:
                         grid.correct(4)
                    elif event.key == pygame.K_5:
                         grid.correct(5)
                    elif event.key == pygame.K_6:
                         grid.correct(6)
                    elif event.key == pygame.K_7:
                         grid.correct(7)
                    elif event.key == pygame.K_8:
                         grid.correct(8)
                    elif event.key == pygame.K_9:
                         grid.correct(9)
                    elif event.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:  
                         grid.grid[row][col] = 0
                    elif event.key == pygame.K_ESCAPE:  
                         grid.deselect()
                         selected_cell = None
            grid.draw_board()
            pygame.display.update()
        pygame.quit()

    

play_game()



        


        
