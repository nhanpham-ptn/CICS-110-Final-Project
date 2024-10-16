from Checking import is_square_safe, are_columns_safe, are_rows_safe, are_squares_safe, checking
from Sudoku_Generation import generate_board


import pygame

pygame.font.init()

white = (255,255,255)
Black = (0, 0, 0)


window = pygame.display.set_mode((510, 540))
pygame.display.set_caption("SUDOKU")
number = pygame.font.SysFont('Times new Roman', 40)
window.fill(white)

#drawing the board

grid = generate_board()

def board(grid):
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 2
        pygame.draw.line(window,Black, (0, i*(510/9)), (510, i * (510/9)), thickness)
        pygame.draw.line(window,Black, (i*(510/9),0), (i * (510/9), 510), thickness)

    for row in range(9):
        for column in range(9):
            if grid[row][column] != 0:
                text = number.render(str(grid[row][column]), True, Black)
                window.blit(text, (column * 510/9 +19, row * 510/9+ 8))
run = True
while run:
    for event in pygame.event.get():
        board(grid)
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()