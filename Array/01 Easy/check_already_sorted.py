def check_already_sorted(arr):
    sorted = False
    for i in range(0,len(arr)-1):
        if arr[i] <= arr[i+1]:
            sorted = True
        else:
            sorted = False
            break
    print(sorted)

check_already_sorted([1,2,3,4,5])
check_already_sorted([5,4,3,2,1])
    