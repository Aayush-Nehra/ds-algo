def partition(arr, start, end):
    pivot_pos = start
    pivot_element = arr[end]
    for i in range(start, end):
        if arr[i] < pivot_element:
            arr[i], arr[pivot_pos] = arr[pivot_pos], arr[i]
            pivot_pos += 1
    arr[pivot_pos], arr[end] = arr[end], arr[pivot_pos]
    return pivot_pos

# a = [6, 7, 2, 1, 5]
# pivot_postion = find_pivot(a, 0, len(a)-1)
# print(f"Array with one element at correct place {a}, Pivot pos = {pivot_postion}")

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)

a = [4,1,7,9,3]

quicksort(a, 0, len(a)-1)

print(a)