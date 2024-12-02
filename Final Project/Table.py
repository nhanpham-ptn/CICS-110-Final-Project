from Checking import checking, making_game
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
        self.board = create_board() 
        self.grid = making_game([row[:] for row in self.board]) 
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
        font = pygame.font.SysFont('Arial', 30)
        attempts = font.render(f"Errors: {self.attempt}", True, Black)
        attempt_rec = attempts.get_rect(center=(70, 550))
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
            if checking(self.board, num, row, col):
                self.grid[row][col] = num  
                cell = pygame.Rect(col * (510 / 9), row * (510 / 9), (510 / 9), (510 / 9))
                pygame.draw.rect(self.window, green, cell, 5)
                pygame.display.update()
                pygame.time.delay(300)
                return True
            else:
                cell = pygame.Rect(col * (510 / 9), row * (510 / 9), (510 / 9), (510 / 9))
                pygame.draw.rect(self.window, red, cell, 5)
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
    

#To-do list: give an end to the game, timing function, getting attempts


def play_game():
    grid = Board(window)
    selected_cell = None
    run = True

    print("Complete Board:")
    for row in grid.board:
        print(row)
    print("\nPlayable Board:")
    for row in grid.grid:
        print(row)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < 510 and pos[1] < 510:
                        selected_cell = grid.select(pos)
                        (row, col) = selected_cell
                        if grid.grid[row][col] != 0:
                            grid.deselect()
            elif event.type == pygame.KEYDOWN and selected_cell:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                 pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]: 
                    num = event.key - pygame.K_0 
                    grid.correct(num)
                    if not grid.correct(num):
                        grid.attempt -= 1
                run = grid.end()
                if run == False:
                    font = pygame.font.SysFont('Arial', 100)
                    result = font.render("You Win", True, green)
                    result_rec = result.get_rect(center=(255, 255))
                    window.blit(result, result_rec)
                    pygame.display.update()
                    pygame.time.delay(1500) 


        grid.draw_board()
        pygame.display.update()


    pygame.quit()
play_game()


        


        
