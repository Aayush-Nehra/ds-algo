arr = [7, 1, 3, 2, 4, 9, 8]
def insertion_sort(array):
    for i in range(1, len(array)):
        pos = i
        for j in range(0, i):
            if array[pos] < array[pos-1]:
                array[pos], array[pos - 1] = array[pos - 1], array[pos]
                pos = pos - 1
        
        print(f"Run {i}: {array}")
    
    print("Sorted Array: ", array)

insertion_sort(arr)

def insertion_sort2(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Move elements of array[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Usage
array2 = [5, 2, 9, 1, 5, 6]
insertion_sort2(array2)
print("Sorted array is:", array2)