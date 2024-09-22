def lower_bound(nums, target):
    if target > nums[len(nums)-1]:
        return len(nums)
    
    if target < nums[0]:
        return 0
    
    start = 0
    end = len(nums) - 1
    lb = -1
    while start<=end:
        mid = (start+end)//2
        
        if target == nums[mid]:
            while(mid != -1 and nums[mid]==target):
                mid = mid - 1
            return mid +1
        elif target > nums[mid]:
            start = mid + 1
        else:
            lb = mid
            end = mid - 1

    return lb

def lower_bound(nums, target):
    if target > nums[len(nums)-1]:
        return len(nums)
    
    if target < nums[0]:
        return 0
    
    start = 0
    end = len(nums) - 1
    lb = -1
    while start<=end:
        mid = (start+end)//2
        
        if target == nums[mid]:
            lb = mid
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            lb = mid
            end = mid - 1

    return lb


a = [1,2,3,3,7,8,9,9,9,11]
lb = lower_bound(a, 1)
print(a[lb], lb)
# print(lower_bound([3,5,8,15,19], 9))