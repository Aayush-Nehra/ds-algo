def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        high = mid - 1
    else:
        low = mid + 1

    return recursive_binary_search(arr, low, mid, target)

arr = [-1,0,3,5,9,12]
print(recursive_binary_search(arr, 0, len(arr)-1, 0))