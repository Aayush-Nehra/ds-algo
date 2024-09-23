def generate(numRows):
    pascal_triangle = [[1],[1,1]]
    current_row = []
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return pascal_triangle
    else:
        for i in range(2, numRows):
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    current_row.append(1)
                else:
                    element = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
                    current_row.append(element)
            pascal_triangle.append(current_row)
            current_row = []
    return pascal_triangle

print(generate(5))