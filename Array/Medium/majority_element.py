#Approach 1 Brute Force
#  - Sort the array and scan 
#If element occurs more than n/2 times while scan then that is majority element

def majority_element(nums):
    freqMap = {}
    size = len(nums)
    for num in range(size):
        if nums[num] in freqMap:
            freqMap[nums[num]] += 1
        else:
            freqMap[nums[num]] = 1
    # I can combine and work on the above similarly as the majority element can be scanned for each element
    majority_size = size // 2

    for num in freqMap:
        if freqMap[num] > majority_size:
            return num
        
    return -1

def majority_elemet3(nums):
    """Moore's voting algorithm"""
    majority_num = nums[0]
    count = 1

    for i in range(1, len(nums)):
        if nums[i] != majority_num:
            count -= 1
        else:
            count += 1

        if count == 0:
            majority_num = nums[i]
            count += 1
    
    return majority_num

