import math
def getDivisionSum(divisor, nums):
    curDivSum = 0
    for num in nums:
        curDivSum += math.ceil(num/divisor)

    return curDivSum

def smallestDivisor(nums, threshold):
    low = 1
    high = max(nums)

    while low <= high:
        mid = (low + high)//2
        divSum = getDivisionSum(mid, nums)

        if divSum <= threshold:
            ans = mid
            high = mid - 1
        elif divSum > threshold:
            low = mid + 1
    
    return ans
