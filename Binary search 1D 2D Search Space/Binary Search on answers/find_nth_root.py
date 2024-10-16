def find_nth_root_linear(num, N):
    for i in range(1,num):
        if i ** N == num:
            return i
        elif i**N > num:
            return -1
        
    return -1

def find_nth_root_binary(num, N):
    low = 1
    high = N

    while low<=high:
        mid = (low + high) // 2
        if mid ** N == num:
            return mid
        elif mid ** N > num:
            high = mid - 1
        else: 
            low = mid + 1

    return -1

print(find_nth_root_linear(28, 3))
print(find_nth_root_binary(27, 3))
print(find_nth_root_binary(28, 3))