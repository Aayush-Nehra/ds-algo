def findMin(nums):
    minimum = 99999
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high)//2

        if nums[mid]<=nums[high]:
            minimum = min(nums[mid], minimum)
            high = mid - 1
        else:
            minimum = min(nums[low], minimum)
            low = mid + 1

    print(minimum)
    return minimum

a = [3,4,5,1,2]
findMin(a)