def upper_bound(arr, n, x):
    ans = len(arr) - 1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

a = [1 ,4, 7, 8, 10]
upper_bound(a, 5, 7)
