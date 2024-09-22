def subarraySum(nums,k):
    """Brute force"""
    no_of_subarrays = 0
    size = len(nums)
    sum = 0
    for i in range(size):
        for j in range(i, size):
            sum += nums[j]
            if sum == k:
                no_of_subarrays += 1
        sum = 0

    return no_of_subarrays

def subarraySum2(nums, k):
    prevSum = {}
    n = 0
    sum = 0
    size = len(nums)

    for i in range(0, size):
        sum += nums[i]
        if sum == k:
            n += 1

        diff = sum - k

        if diff in prevSum:
            n += prevSum[diff] 

        if sum not in prevSum:
            prevSum[sum] = 1
        else:
            prevSum[sum] += 1

subarraySum2([1], 0)