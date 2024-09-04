def merge(arr1, arr2):
    i, j = 0, 0
    merged_array = []
    while i < len(arr1) and j<len(arr2):
        if(arr1[i]<arr2[j]):
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # if i < len(arr1):
    #     while i < len(arr1) :
    #         merged_array.append(arr1[i])
    #         i += 1
    
    # if j < len(arr2):
    #     while j < len(arr2) :
    #         merged_array.append(arr2[j])
    #         j += 1
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])

    return merged_array

def merge_sort(arr, start_index, end_index):
    if start_index == end_index:
        return [arr[start_index]]
    mid = (start_index + end_index)//2
    arr1 = merge_sort(arr, start_index, mid)
    arr2 = merge_sort(arr, mid + 1, end_index)
    merged_arr = merge(arr1, arr2)
    return merged_arr

# arr1 = [1,3,5,7]
# arr2 = [2,4,6,7,9]
# merge(arr1, arr2)

unsorted_list = [34, 7, 23, 32, 5, 62, 3, 21, 44, 9]
sorted_list = merge_sort(unsorted_list, 0, len(unsorted_list)-1)

print(sorted_list)

