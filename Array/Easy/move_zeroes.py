def move_zeroes(nums):
    non_zero_pos = 0
    countZeroes = 0
    size = len(nums)
    for i in range(size):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1
        else:
            countZeroes += 1    

    for i in range(0, countZeroes):
        nums[size-countZeroes+i] = 0
        
    print(nums)

def move_zeroes2(nums):
    zero_pos = -1
    size = len(nums)

    for i in range(size):
        if nums[i] == 0:
            zero_pos = i
            break

    for i in range(zero_pos+1, size):
        if nums[i] != 0:
            nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
            zero_pos += 1

    print(nums)

nums = [0,1,0,3,12]
#nums = [2, 1]
move_zeroes2(nums)
