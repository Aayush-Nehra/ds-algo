#1 Generate element based on row,column of pascal triangle. 
#       Each element of a pascal triangle represents binomial coefficient in 0 based index. 
#       Element 7,4 will be (n-1)C(r-1) i.e 6C4
#       So to find element we need to provide (n-1) C (r-1)

def genNcR(row, column):
    res = 1
    for i in range(1, column+1):
        res = res * row
        res //= i
        row = row - 1
    return res

def pascalElement(row, column):
    return genNcR(row-1, column-1)

# print(pascalElement(1,1))
# print(pascalElement(5,2))
# print(pascalElement(6,2))

def createPascalRow(row):
    pascalRow = []
    for i in range(1,row+1):
        pascalRow.append(pascalElement(row, i))
    print(pascalRow)

def createPascalRows(rows):
    pascalRows = []
    res = 1
    for i in range(rows):
        pascalRow = [1]
        for j in range(1, i+1):
            res *= (i + 1) -j
            res //= j
            pascalRow.append(res)
        pascalRows.append(pascalRow)

    print(pascalRows)
        

createPascalRows(6)








