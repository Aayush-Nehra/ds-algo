def findPagesRange(arr):
    minPages = -1
    maxPages = 0

    for pages in arr:
        #This is wrong, max pages should be our low
        # if pages < minPages:
        #     minPages = pages
        if pages > minPages:
            minPages = pages
        maxPages += pages

    return (minPages, maxPages)

def checkPageAllocationPossible(arr, minPages, m):
    currentStudentPageAllocation = 0
    i = 0
    allocatedStudent = 0
    while i < len(arr) and allocatedStudent<m:
        currentStudentPageAllocation += arr[i]
        if currentStudentPageAllocation <= minPages:
            i += 1
        else:
            allocatedStudent += 1
            currentStudentPageAllocation = arr[i]
            if currentStudentPageAllocation > minPages:
                return False
            i += 1
            
    if i == len(arr) and allocatedStudent < m:
        print("Yes")
        return True
    else:
        print("No")
        return False

def findPages(arr, n, m):
    if n < m:
        return -1

    low, high = findPagesRange(arr)

    while low <= high:
        mid = (low + high)//2

        if checkPageAllocationPossible(arr, mid, m):
            high = mid - 1
        else:
            low = mid + 1
    print(low)
    return low

arr = [25, 46, 28, 49, 24]
m = 4
n = 5

m = 7 
n = 7
arr = [1, 17, 14, 9, 15, 9, 14] 


#checkPageAllocationPossible(arr, 70, 4)
findPages(arr, n, m)



