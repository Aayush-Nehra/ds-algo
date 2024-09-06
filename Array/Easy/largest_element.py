largest = 0
arr = [1, 2, 9, 5, 4, 7, 6]
arr2 = [5,5,5,5]

for i in arr:
    if i > largest:
        largest = i

print(largest)

#largest using recursion

def find_largest(arr, pos ,n, largest):
    if pos == n:
        return largest
    if(arr[pos] >= largest):
        largest = arr[pos]
    return find_largest(arr, pos+1, n, largest)

print(find_largest(arr2, 0, len(arr2), 0))

    