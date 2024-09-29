def removeDuplicates(nums):
    if len(nums) == 1:
        return 1
    k = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[k]: #nums k is previous unique number
            k += 1
            nums[k] = nums[i]
    
    return k + 1

# nums1 = [1,1,2]
nums1 = [1]
k1 = removeDuplicates(nums1)
print(f"K1 = {k1}, nums1 = {nums1}")

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = removeDuplicates(nums2)
print(f"K2 = {k2}, nums2 = {nums2}")

nums3 = [1,2,3,4,5]
k3 = removeDuplicates(nums3)
print(f"K = {k3}, nums = {nums3}")