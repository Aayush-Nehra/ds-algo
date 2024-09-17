def find_leaders(nums):
    size = len(nums)
    leaders = [nums[size-1]]
    max_in_list = nums[size-1]
    for i in range(size-2,-1,-1):
        if nums[i] > max_in_list:
            leaders.append(nums[i])
        max_in_list = max(nums[i], max_in_list)

    print(leaders)

find_leaders([10, 22, 12, 11, 11, 11])