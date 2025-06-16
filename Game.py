from Checking import is_valid_move
from Sudoku_Generation import create_board
from Board import Board


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


def difficulty_menu():
    font = pygame.font.SysFont('Arial', 50)
    run = True
    difficulty = None

    while run:
        window.fill((255, 255, 255))  # white background

        # Render text
        title = font.render("Select Difficulty", True, (0, 0, 0))
        easy_text = font.render("1 - Easy", True, (0, 255, 0))
        medium_text = font.render("2 - Medium", True, (255, 165, 0))
        hard_text = font.render("3 - Hard", True, (255, 0, 0))

        # Draw text to screen
        window.blit(title, (100, 50))
        window.blit(easy_text, (150, 150))
        window.blit(medium_text, (150, 250))
        window.blit(hard_text, (150, 350))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "easy"
                    run = False
                elif event.key == pygame.K_2:
                    difficulty = "medium"
                    run = False
                elif event.key == pygame.K_3:
                    difficulty = "hard"
                    run = False

    return difficulty

#Don't turn on UniKey while playing or else, it won't work
def play_game():
    # Call the menu first
    difficulty = difficulty_menu()

    grid = Board(window, difficulty)
    selected_cell = None
    run = True
    font = pygame.font.SysFont('Arial', 100)

    print("complete board:")
    for row in grid.board:
        print(row)
    print("\nplayable board:")
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
                    if grid.attempt == 0:
                        result = font.render("You Lose", True, red)
                        result_rec = result.get_rect(center=(255, 255))
                        window.blit(result, result_rec)
                        pygame.display.update()
                        pygame.time.delay(1500)
                        play_game()

                run = grid.end()
                if run == False:
                    result = font.render("You Win", True, green)
                    result_rec = result.get_rect(center=(255, 255))
                    window.blit(result, result_rec)
                    pygame.display.update()
                    pygame.time.delay(1500)
                    play_game()

        grid.draw_board()
        pygame.display.update()

    pygame.quit()


play_game()