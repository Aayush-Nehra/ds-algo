def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = (low+high)//2

        if (mid+1)< len(nums) and nums[mid+1] == nums[mid]:
            if (high-mid-1)%2 == 0:
                high = mid-1
            else:
                low = mid + 2
        elif (mid-1) > -1 and nums[mid-1] == nums[mid]:
            if (mid-1) % 2 == 0:
                low = mid + 1
            else:
                high = mid-2
        else:
            return nums[mid] 
        
a = [1,1,2]
singleNonDuplicate(a)