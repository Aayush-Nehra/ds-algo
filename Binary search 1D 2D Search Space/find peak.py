def findPeakElement(nums):
    low = 1
    high = len(nums) - 2

    if len(nums) == 1:
        return 0
            
    if nums[0] > nums[1]:
        return 0
    if nums[high]<nums[high+1]:
        return high + 1


    while low <= high:
        mid = (low + high)//2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid-1] <= nums[mid] and nums[mid] <= nums[mid+1]:
            low = mid + 1
        elif nums[mid-1] >= nums[mid] and nums[mid] >= nums[mid+1]:
            high = mid - 1
        else:
            low -= 1
            high -= 1

    return -1

#findPeakElement([6,5,4,3,2,3,2])
findPeakElement([1,2,1,2,1])




