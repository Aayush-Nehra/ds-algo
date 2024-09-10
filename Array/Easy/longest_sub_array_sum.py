def longest_sub_array_sum(nums, k):
    longest_sub_array = []
    current_sub_array = []
    currentSum = 0
    size = len(nums)

    for i in range(0, size):
        for j in range(i, size):
            currentSum += nums[j]
            current_sub_array.append(nums[j])
            if currentSum == k:
                if len(current_sub_array)>len(longest_sub_array):
                    longest_sub_array = current_sub_array[:]
            if currentSum > k:
                currentSum = 0
                current_sub_array = []
                print(longest_sub_array)
                break

    print(longest_sub_array)

a = [2,3,5,1,9]
k = 10

longest_sub_array_sum(a, k)
                