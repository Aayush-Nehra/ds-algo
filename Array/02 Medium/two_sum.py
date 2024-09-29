from typing import List

def two_sum(nums, target):
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum2(nums, target):
    """Solution with hash map"""
    hashMap = {}
    size = len(nums)
    for i in range(size):
        hashMap[nums[i]] = i

    for i in range(size):
        diff = target - nums[i]
        if diff in hashMap and hashMap[diff] != i:
            return [hashMap[diff], i]
        
def twoSum3(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # {7: 0}
        for i, n in enumerate(nums): # [2,7] 1, 7
            rem = target - n # 7
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[n] = i 
        

print(two_sum([25,17,2,7], 9))
#print(two_sum())