# CHECK THE GAME
# checking rows
def are_rows_safe(grid):
    result = True
    for i in range(9):
        nums = [1,2,3,4,5,6,7,8,9]
        for j in grid[i]:
            if j in nums:
                nums.remove(j)
                pass
            else:
                result = False
    return result

#checking columns
def are_columns_safe(grid):
    result = True
    for i in range(9):
        rows = []
        nums = [1,2,3,4,5,6,7,8,9]

        for j in range(9):
            rows.append(grid[j][i])
        for n in rows:
            if n in nums:
                nums.remove(n)
                pass
            else:
                result = False
    return result


#checking squares
def is_square_safe(grid, x, y):
    result = True
    nums= [1,2,3,4,5,6,7,8,9]

    for i in range(3):
        for j in range(3):
            if grid[i +3*y][j + 3*x] in nums:
                nums.remove(grid[i +3*y][j + 3*x])
            else:
                result = False
    return result



def are_squares_safe(grid):
    result = True
    for y in range(3):
        for x in range(3):
            result = is_square_safe(grid,x,y)
    return result


#checking all
def checking(grid):
    if are_columns_safe(grid) == True:
        if are_rows_safe(grid) == True:
            if are_squares_safe(grid) == True:
                return True
    else:
        return False

