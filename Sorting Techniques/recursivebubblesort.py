def rbubble_sort(arr, run_count=0):
    did_swap = False
    if run_count == len(arr)-1:
        return
    for i in range(0, len(arr)-1-run_count):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            #To optimise
            did_swap = True

    if(not did_swap):
        return
    print(arr)
    run_count += 1
    rbubble_sort(arr, run_count)

arr = [34, 7, 23, 32, 5, 62, 3, 21, 44, 9]

rbubble_sort(arr)

print(f"Sorted Array: {arr}")