def max_sub_array(nums):
    maxSum = None
    curSum = 0
    size = len(nums)
    for i in range(size):
        for j in range(i,size):
            curSum += nums[j]
            if maxSum == None or curSum > maxSum:
                maxSum = curSum

        #print(f"Max sum for {i}: {maxSum}")
        curSum = 0

    return maxSum

def max_sub_array2(nums):
    """Kadanes algorithm"""
    sum = 0
    max = -999999
    size = len(nums)
    for i in range(size):
        sum += nums[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0

    return max

def max_sub_Array_sum_with_array(nums):
    sum = 0
    max = -999999
    size = len(nums)
    start, end = -1, -1
    start_ind = -1
    for i in range(size):
        if sum == 0:
            start = i
        sum += nums[i]

        if sum > max:
            start_ind = start
            max = sum
            end = i
        if sum < 0:
            sum = 0

    print(nums[start_ind:end+1])
    print(max)

    
a = [-2,1,-3,4,-1,2,1,-5,4]
# a = [1]
#a = [5,4,-1,7,8]
# This is brute force but for lage inputs it gives TLE.
# Think of better algo
#a = [-2, 1]
print(max_sub_Array_sum_with_array(a))