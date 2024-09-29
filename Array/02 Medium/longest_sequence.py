def find_longest_sequence(nums):
    """Better solution"""
    nums.sort()
    longest_sequence = 0
    current_sequence = 0
    for i in range(0, len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            current_sequence += 1
        else:
            current_sequence = 1
            
        longest_sequence = max(current_sequence, longest_sequence)
    
    print(longest_sequence)

def find_longest_sequence2(nums):
    hashSet = set(nums)
    found = True
    x = -9999
    current_sequence = 1
    longest_sequence = 1
    for num in hashSet:
        if num-1 in hashSet:
            continue
        else:
            x = num
            while found:
                if x+1 in hashSet:
                    x += 1
                    current_sequence += 1
                else:
                    found = False
        longest_sequence = max(current_sequence,  longest_sequence)
        current_sequence = 1
        found = True

    print(longest_sequence)






find_longest_sequence2([3, 8, 5,5,5, 7,7,7,7, 6, 11,12,13,14,15,16,16])
