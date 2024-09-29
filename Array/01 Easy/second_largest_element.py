def find_second_largest_element(arr):
    largest = 0
    second_largest = -1
    for current_num in arr:
        if current_num > largest:
            second_largest = largest
            largest = current_num
        elif current_num > second_largest:
            second_largest = current_num

    print(f"Largest: {largest}, \n Second Largest: {second_largest}")

find_second_largest_element([5,1,7,2,8])
            