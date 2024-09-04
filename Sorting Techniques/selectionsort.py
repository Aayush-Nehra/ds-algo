arr = [7, 1, 3, 2, 4, 9, 8]
def selection_sort(array):
    smallest_index = 9999
    for i in range(0, len(array)):
        smallest = array[i]
        for j in range(i, len(array)):
            if array[j] <= smallest:
                smallest = arr[j]
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], arr[i]
        print(f"Run {i}: {array}")
    
    print("Sorted Array: ", array)

selection_sort(arr)