def spiral_order(matrix):
    """Prints in spiral order"""
    first_row = 0
    last_col = len(matrix[0]) # n
    last_row = len(matrix) # m
    first_col = 0
    spiral = []
    added = True
    while True:
        for j in range(first_col, last_col):
            spiral.append(matrix[first_row][j])
            matrix[first_row][j] = 'v'
            added = True
    
        if added == False:
            break
        added = False
        first_row += 1
        
        for i in range(first_row, last_row):
            spiral.append(matrix[i][last_col-1])
            matrix[i][last_col-1] = 'v'
            added = True
        
        if added == False:
            break
        added = False
        last_col -= 1

        for j in range(last_col-1, first_col-1, -1):
            spiral.append(matrix[last_row-1][j])
            matrix[last_row-1][j] = 'v'
            added = True
        
        if added == False:
            break
        added = False
        last_row -= 1

        for i in range(last_row-1, first_row-1, -1):
            spiral.append(matrix[i][first_col])
            matrix[i][first_col] = 'v'
            added = True

        if added == False:
            break
        added = False
        first_col += 1



    print(spiral)


spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])            