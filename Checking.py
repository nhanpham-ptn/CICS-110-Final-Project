# CHECK THE GAME
import random


def is_valid_move(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True







'''
# checking rows

def are_rows_safe(grid, num, row):
    result = True
    for j in grid[row]:
        if num != 0:
            if j == num:
                result = False
    return result

#checking columns
def are_columns_safe(grid, num, col):
    for i in range(9):  
        if num != 0:  
            if grid[i][col] == num  :
                return False  
    return True  


#checking squares
def is_square_safe(grid, num, col, row):
    start_col = int(col//3)*3
    start_row = int(row//3)*3
    if num !=0:
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
    return True

#checking all
def checking(grid, num, row, col):
    return are_rows_safe(grid, num, row) and are_columns_safe(grid, num, col) and is_square_safe(grid, num, col, row)

board = [[4, 6, 1, 3, 2, 5, 7, 8, 9],
         [0, 0, 0, 0, 4, 9, 0, 3, 0],
         [9, 0, 0, 0, 8, 0, 2, 4, 0],
         [2, 8, 0, 0, 9, 0, 4, 0, 7],
         [1, 7, 0, 0, 0, 0, 8, 2, 5],
         [0, 0, 0, 2, 7, 0, 9, 1, 3],
         [0, 0, 0, 0, 5, 0, 3, 9, 0],
         [8, 0, 0, 7, 0, 3, 6, 5, 4],
         [0, 0, 4, 0, 0, 2, 1, 7, 0]]

def get_location():
     row = int(input("Enter a row:"))
     col = int(input("Enter a col:"))
     return (row,col)

def filling_num(board):
        (row, col) = get_location()
        num = int(input("Enter a number"))
        if board[row][col] == 0:
         if checking(board, num, col, row):
             board[row][col] = num
             print("Correct")
         else:
             print("Incorrect")
         return None


def result(board):
     for row in range(9):
         for col in range(9):
             if board[row][col] == 0:
                 return False
     return True

run = True

while run:
     for row in board:
         print(row)
     filling_num(board)
     if result(board):
         run = False
'''
