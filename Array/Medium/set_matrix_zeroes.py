def setZeroes(matrix):
    """Better approach using set"""
    m = len(matrix)
    n = len(matrix[0])
    row_set = set()
    column_set = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_set.add(i)
                column_set.add(j)

    #print(row_set, column_set)
    for row in row_set:
        for j in range(n):
            matrix[row][j] = 0

    for column in column_set:
        for i in range(m):
            matrix[i][column] = 0

def setZeroes2(matrix):
    """Optimal approach using representative element"""
    def make_row_z(row, n):
        for j in range(n):
            if matrix[row][j] != 0:
                matrix[row][j] = 'z'
    
    def make_col_z(col, m):
        for i in range(m):
            if matrix[i][col] != 0:
                matrix[i][col] = 'z'
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                make_row_z(i, n)
                make_col_z(j, m)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'z':
                matrix[i][j] = 0

    


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

setZeroes2(matrix)
print(matrix)
