# CHECK THE GAME
# checking rows

grid = [[6.9,5,1,2,3,4,7,8],
        [7,2,4,8,6,5,1,9,3],
        [3,8,1,7,4,9,6,2,5],
        [9,3,7,4,1,2,8,5,6],
        [8,4,2,6,5,7,9,3,1],
        [5,1,6,3,9,8,7,4,2],
        [2,7,3,9,8,1,5,6,2],
        [4,5,8,2,7,6,3,1,9],
        [1,6,9,5,3,4,2,8,7]
        ]

def are_rows_safe(grid, num, row):
    result = True
    for j in grid[row]:
        if num != 0:
            if num == j:
                result = False
    return result

#checking columns
def are_columns_safe(grid, num, col):
    for i in range(9):  
        if num != 0:  
                if num ==  grid[i][col]:
                    return False  
    return True  


#checking squares
def is_square_safe(grid, num, col, row):
    result = True
    for i in range(3):
        for j in range(3):
            if num !=0:
                if num == grid[i +3*col][j + 3*row]:
                    result = False
    return result


#checking all
def checking(grid, num, col, row):
    return are_rows_safe(grid, num, row) and are_columns_safe(grid, num, col) and is_square_safe(grid, num, col, row)

