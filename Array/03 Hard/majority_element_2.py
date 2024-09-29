def majority_element(nums):
    """Hashing"""
    freqDict = {}
    majority_size = len(nums)//3
    ans = []
    for num in nums:
        if num not in freqDict:
            freqDict[num] = 1
        else:
            freqDict[num] += 1

    for num in freqDict:
        if freqDict[num] > majority_size:
            ans.append(num)

    return ans

def majority_element(nums):
    """Linear space and time"""