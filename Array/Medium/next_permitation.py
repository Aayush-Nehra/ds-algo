def next_permutation(nums):
    size = len(nums)
    breakingIndex = -1
    swapIndex = -1
    for i in range(size-2, -1, -1):
        if nums[i] < nums[i+1]:
            breakingIndex = i
            break

    if breakingIndex == -1:
        nums.reverse()
    else:
        for i in range(size-1, -1, -1):
            if nums[i] > nums[breakingIndex]:
                swapIndex = i
                break

        nums[breakingIndex], nums[swapIndex] = nums[swapIndex], nums[breakingIndex]
        nums[breakingIndex+1:] = nums[breakingIndex+1:][::-1]
        
nums = [1,3,2]
next_permutation(nums)
print(nums)