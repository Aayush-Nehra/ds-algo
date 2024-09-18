def rotate(matrix):
    n = len(matrix)
    #n = len(matrix[0])

    swap_rows = n//2

    #Invert matrix
    for i in range(swap_rows):
        for j in range(n):
            matrix[i][j],matrix[n-i-1][j]  = matrix[n-i-1][j],matrix[i][j]

    # Replace diagonals
    for i in range(n):
        for j in range(n):
            if i == j or i>j:
                continue
            else:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)

rotate([[1,2,3],[4,5,6],[7,8,9]])
rotate([[1,2],[3,4]])