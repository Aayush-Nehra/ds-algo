def search(nums, target):
    low = 0 
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[low] > target and nums[low] > nums[high]:
                low = low + 1
            else:
                high = mid - 1
        else:
            if nums[high] < target and nums[low] > nums[high]:
                high = high -1
            else:
                low = mid + 1

    return -1

def search2(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            print(True)
            return True

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    print(False)
    return False
# nums = [4,5,6,7,0,1,2] 
# target = 0
# #target = 3
# print(search(nums, target))
# nums = [5,1,3]
# target = 5
# print(search(nums, target))
nums = [5,1,2,3,4]
nums = [1,0,1,1,1]
target = 0
print(search(nums, target))

