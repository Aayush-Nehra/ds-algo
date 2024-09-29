from typing import List


def left_rotate_arr(nums):
    last_num = nums[0]

    for i in range(0, len(nums)-1):
        nums[i] = nums[i+1]

    nums[-1] = last_num
    print(nums)

#optimal left rotation can also be done by 3 reversals

def right_rotate_arr(nums):
    last_num = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        nums[i+1] = nums[i]

    nums[0] = last_num
    print(nums)

def right_rotate_arr_k_times(nums, k):
    for i in range(0,k):
        right_rotate_arr(nums)

    print(nums)


#Better is using enq and dq
def rotate(self, nums: List[int], k: int) -> None:
    if k == 0:
        return

    size = len(nums)
    k = k if k <= size else k % size
    
    nums[k:], nums[:k] = nums[:size - k], nums[size - k:]

#Most optimal is using slice operation
def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return

        size = len(nums)
        k = k if k <= size else k % size
        
        nums[k:], nums[:k] = nums[:size - k], nums[size - k:]


nums = [1,2,3,4,5]
# left_rotate_arr(nums)
# right_rotate_arr(nums)

right_rotate_arr_k_times(nums, 3)

