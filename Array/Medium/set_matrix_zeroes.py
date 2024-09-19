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
    """Brute force using representative element""" 
    #TC = O(n**3)
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

    
def setZeroes3(matrix):
    """Make first row and first column of matrix as indicator for tracking zeroes 
    and have one extra variable for column"""
    m = len(matrix)
    n = len(matrix[0])
    col0 = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j == 0:
                    col0 = 0
                else:
                    matrix[0][j] = 0
    #Leaving first row and column make other elements as 0
    print(matrix)
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    #Deal with first row except first element
    if matrix[0][0] == 0:
        for i in range(1,n):
                matrix[0][i] = 0

    #Deal with first column
    for i in range(m-1,0,-1):
        if col0 == 0:
            matrix[i][0] = 0

    print(matrix)

    

matrix = [[0,1,2,0],[3,4,5,2],[1,3,0,5]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes3(matrix)
print(matrix)
