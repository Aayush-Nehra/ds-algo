def rinsertion_sort(arr, key_i):
    if key_i == len(arr):
        return
    j = key_i - 1
    key = arr[key_i]
    while arr[j] > key and j>=0:
        arr[j+1] = arr[j] #Yaha element aage shift kar rahe ho islea j+1 = j
        j -= 1
    arr[j+1] = key # Jab loop k bahar aae to element aage badh jata hai islea esa karna padhta hai
    rinsertion_sort(arr, key_i + 1)

arr = [34, 7, 23, 32, 5, 62, 3, 21, 44, 9]

rinsertion_sort(arr, 1)

print(f"Sorted Array: {arr}")