def find_max_consecutive_ones(nums):
    max1s = 0
    consecutive1s = 0

    for num in nums:
        if num == 1:
            consecutive1s += 1
            if consecutive1s > max1s:
                max1s = consecutive1s
        if num == 0:
            consecutive1s = 0

    return max1s

print(find_max_consecutive_ones([0]))
print(find_max_consecutive_ones([1]))
print(find_max_consecutive_ones([0,1,1,0,1,0,1,1,0]))