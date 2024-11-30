# CHECK THE GAME
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
def checking(grid, num, col, row):
    return are_rows_safe(grid, num, row) and are_columns_safe(grid, num, col) and is_square_safe(grid, num, col, row)



from Sudoku_Generation import create_board

board = create_board()

# def get_location():
#     row = int(input("Enter a row:"))
#     col = int(input("Enter a col:"))
#     return (row,col)

# def filling_num(board):
#     (row, col) = get_location()
#     num = int(input("Enter a number"))
#     if board[row][col] == 0:
#         if checking(board, num, col, row):
#             board[row][col] = num
#             print("Correct")
#         else:
#             print("Incorrect")
#     return None


# def result(board):
#     for row in range(9):
#         for col in board[row]:
#             if board[row][col] == 0:
#                 return False
#     return True

# run = True

# while run:
#     for row in board:
#         print(row)
#     filling_num(board)
#     if result(board):
#         run = False
