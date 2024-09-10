def missing_number(nums):
    sum_of_nums = sum([num for num in nums])
    n = len(nums)
    sum_first_n = (n * (n + 1))/2

    return sum_first_n - sum_of_nums