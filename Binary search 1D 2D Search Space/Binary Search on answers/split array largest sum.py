def findRange(nums):
    max = -1
    total = 0

    for num in nums:
        if num > max:
            max = num
        total += num

    return (max, total)

def findNoOfSplitPossible(nums, maxSum):
    n = 0
    curSum = 0
    for i in range(len(nums)):
        if curSum + nums[i] <= maxSum:
            curSum += nums[i]
            i = i+1
        else:
            n += 1
            curSum = nums[i]
    # print(n + 1)
    return n + 1

def splitArray(nums, k):
    low, high = findRange(nums)

    while low <= high:
        mid = (low + high)//2
        splits = findNoOfSplitPossible(nums, mid)
        if splits > k:
            low = mid + 1
        else:
            high = mid - 1
    print(low)
    return low


nums = [7,2,5,10,8] 
maxSum = 35
k = 2

# findNoOfSplitPossible(nums, maxSum)
splitArray(nums, k)

