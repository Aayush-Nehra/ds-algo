arr = [7, 1, 3, 2, 4, 9, 8]
swap_flag = False
def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(1, len(array)-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                swap_flag = True
        print(f"Run {i}: {array}")
        if(not swap_flag):
            break
        else:
            swap_flag = False
    
    print("Sorted Array: ", array)

bubble_sort(arr)