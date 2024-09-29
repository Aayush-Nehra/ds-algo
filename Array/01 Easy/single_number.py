def single_number(nums):
    size = len(nums)
    final_num = 0
    if size == 1:
        return nums[0]
    
    for i in range(0, size):
        final_num ^= nums[i]

    return final_num

print(single_number([2,2,1]))
print(single_number([1]))