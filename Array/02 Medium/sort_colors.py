def sortColors(nums) -> None:
    """Sorting approach using three vaiables"""
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            count0 += 1
        elif nums[i] == 1:
            count1 += 1
        else:
            count2 += 1
    nums = []
    while count0 > 0:
        nums.append(0)
        count0 -= 1
    while count1 > 0:
        nums.append(1)
        count1 -= 1
    while count2 > 0:
        nums.append(2)
        count2 -= 1

    print(nums)

def sortColors2(nums):
    """Dutch national flag algorithm"""
    size = len(nums)
    low, mid, high = 0, 0, size-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    print(nums)


sortColors2([2,0,2,1,1,0,0,2,1,1,0])
    
