def threeSumBF(nums):
    """Brute force n3"""
    n = len(nums)
    sum = 0
    ans = set()
    for i in range(n):
        sum += nums[i] 
        for j in range(i+1, n):
            sum += nums[j]
            for k in range(j+1, n):
                sum += nums[k]
                if sum == 0:
                    temp = tuple(sorted([nums[i], nums[j], nums[k]]))
                    ans.add(temp)
                sum -= nums[k]
            sum -= nums[j]
        sum = 0

    return [list(item) for item in ans]

def threeSum2(nums):
    """Ord n sq. hashing approach"""
    ans = set()
    for i in range(len(nums)):
        hashSet  = set()
        for j in range(i+1, len(nums)):
            twoSum = nums[i] + nums[j]
            if -twoSum in hashSet:
                three_sum = tuple(sorted([nums[i], nums[j], -twoSum]))
                ans.add(three_sum)
            hashSet.add(nums[j])
    return [list(item) for item in ans]
    


def threeSum3(arr):
    """fix an element sort = 2 sum"""
    ans = []
    arr.sort()
    n = len(arr)
    for i in range(n):
        # remove duplicates:
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        # moving 2 pointers:
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates:
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans

def threeSum4(nums):
    size = len(nums)
    ans = []
    nums.sort()
    k = size - 1

    for i in range(0, size):
        if i>0 and nums[i] == nums[i-1]:
            continue 
        j = i + 1
        k = size - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                three_sum = [nums[i], nums[j], nums[k]]
                ans.append(three_sum)
                j += 1
                k -= 1
                while j<k and nums[j]==nums[j-1]:
                    j += 1
                while j<k and nums[k]==nums[k+1]:
                    k -=1

    return ans

    




print(threeSum4([-1,0,1,2,-1,-4,-2,-3,3,0,4]))