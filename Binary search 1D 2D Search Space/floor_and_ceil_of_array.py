def floor_and_ceil(nums, target):
    floor = len(nums)
    ceil = len(nums)

    high = len(nums) - 1
    low = 0

    #finding floor
    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            floor = nums[mid]
            break
        elif nums[mid] > target:
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1

    high = len(nums) - 1
    low = 0

    #finding floor
    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            ceil = nums[mid]
            break
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            low = mid + 1

    print(floor, ceil)


nums = [3, 4, 4, 7, 8, 10]

floor_and_ceil(nums, 5)
floor_and_ceil(nums, 8)