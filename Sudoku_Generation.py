import random
#create a board
def create_board():
    board = []
    #make an entire board filled of 0s first
    for i in  range(9):
        spaces = []
        for j in range(9):
            spaces.append(0)
        board.append(spaces)
    #fill the board with apropriate numbers in diagonal 3x3 squares
    for i in range(0, 9, 3):
        nums = [1,2,3,4,5,6,7,8,9]
        random.shuffle(nums)
        for row in range(3):
            for column in range(3):
                board[i + row][i + column] = nums.pop()
    # write a function for checking if the number filled is relevant
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
    # write a function filling numbers that have been checked by the function above in all empty cells  
    def fill_cells(board, row, column):
        if row == 9:
            return True
        if column == 9:
            return fill_cells(board, row + 1, 0)
        
        if board[row][column] != 0:
            return fill_cells(board, row, column + 1)
        
    # filling the number from 1 to 9 
        for num in range(1, 10):
            if is_num_safe(board, row, column, num):
                board[row][column] = num
                if fill_cells(board, row, column + 1):
                    return True
        board[row][column] = 0
        return False
    
    fill_cells(board, 0, 0)
    return board