import random


#Generating a board
def generate_board():
    board = []
    for i in  range(9):
        spaces = []
        for j in range(9):
            spaces.append(0)
        board.append(spaces)

    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for row in range(3):
            for column in range(3):
                board[i + row][i + column] = nums.pop()
    

    def is_num_safe(board, row, column, num):
        if num in board[row]:
            return False
        
        for i in range(9):
            if num == board[i][column]:
                return False
        
        start_row = 3 * (row // 3)
        start_column = 3 * (column//3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_column + j] == num:
                    return False
        return True

    def fill_cells(board, row, column):
        if row == 9:
            return True
        if column == 9:
            return fill_cells(board, row + 1, 0)
        
        if board[row][column] != 0:
            return fill_cells(board, row, column + 1)
        

        for num in range(1, 10):
            if is_num_safe(board, row, column, num):
                board[row][column] = num
                if fill_cells(board, row, column + 1):
                    return True
        board[row][column] = 0
        return False
    

    fill_cells(board, 0, 0)

    for i in range(random.randint(55, 65)):
        row = random.randint(0, 8) 
        column = random.randint(0, 8)
        board[row][column] = 0

    return board

board = generate_board()
for row in board:
    print(row)