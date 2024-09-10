# Better brute force
def longest_sub_array_sum(nums, k):
    longest_sub_array = []
    current_sub_array = []
    currentSum = 0
    size = len(nums)

    for i in range(0, size):
        for j in range(i, size):
            currentSum += nums[j]
            current_sub_array.append(nums[j])
            if currentSum == k:
                if len(current_sub_array)>len(longest_sub_array):
                    longest_sub_array = current_sub_array[:]
            if currentSum > k:
                currentSum = 0
                current_sub_array = []
                print(longest_sub_array)
                break

    print(longest_sub_array)

#Optimal - Array = O(n^2)

def longest_sub_array_sum(nums, k):
    prefix_sum_array = [nums[0]]
    size = len(nums)
    maxArrLen = 0
    for i in range(1, size):
        prefix_sum_element = prefix_sum_array[i-1] + nums[i]
        prefix_sum_array.append(prefix_sum_element)

    for i in range(0, size):
        prefixSum = prefix_sum_array[i]
        if prefixSum == k:
            if maxArrLen == 0:
                maxArrLen = i+1
                continue
        for j in range(0, i):
            expSum = prefixSum - prefix_sum_array[j]
            if expSum == k:
                if maxArrLen < i-j:
                    maxArrLen = i-j
            if expSum < k:
                continue
                
    print(maxArrLen)

#Optimal - Hash Map
def longest_sub_array_sum(nums, k):
    """This is better solution. This solution caters to all types of inputs +ve -ve and 0"""
    prevSum = {}
    maxLen = 0
    sum = 0
    size = len(nums)

    for i in range(0, size):
        sum += nums[i]
        if sum == k:
            maxLen = max(maxLen, i+1)

        diff = sum - k

        if diff in prevSum:
            maxLen = max(maxLen, i - prevSum[diff])

        if sum not in prevSum:
            prevSum[sum] = i

    print(maxLen)
                
def longes_sub_array_sum3(nums, k):
    """Most optimal: Two pointer approach""" #Condition is that this solution will only work in case of positives and zero
    left = 0
    right = 0
    sum = nums[0]
    size = len(nums)
    maxLen = 0

    while right < size:
        if sum == k:
            maxLen = max(maxLen, right-left+1)
            right += 1
            if right<size:
                sum += nums[right]
        elif sum < k:
            right += 1
            if right<size:
                sum += nums[right]
        elif sum > k:
            sum -= nums[left]
            left += 1

    print(maxLen)

a = [2,3,5,1,9]
b = [10, 5, 2, 7, 1, 9]
c = [ 1, 2, 1, 0, 1 ]
k = 10

longes_sub_array_sum3(a, 10)
longes_sub_array_sum3(b, 15)
longes_sub_array_sum3(c, 4)
                