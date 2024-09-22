def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start<=end:
        mid = (start + end)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

print(search([-1,0,3,5,9,12], 0))

