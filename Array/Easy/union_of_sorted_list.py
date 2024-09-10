def union_sorted_lists(list1, list2):
    combined_list = list1 + list2
    # Use a set to remove duplicates efficiently
    unique_set = set()
    unique_list = []
    for item in combined_list:
        if item not in unique_set:
            unique_set.add(item)
            unique_list.append(item)
    # Sort the list
    unique_list.sort()
    return unique_list

def union(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    i, j = 0, 0
    union_arr = [-9999]
    while i < size1 and j < size2:
        if arr1[i] < arr2[j]:
            if arr1[i] != union_arr[-1]:
                union_arr.append(arr1[i])
            i += 1    
        elif arr1[i] == arr2[j]:
            if arr1[i] != union_arr[-1]:
                union_arr.append(arr1[i])
            i += 1   
            j += 1
        else:
            if arr2[j] != union_arr[-1]:
                union_arr.append(arr2[j])
            j += 1

    if i < size1:
        while i < size1:
            if arr1[i] != union_arr[-1]:
                union_arr.append(arr1[i])
            i += 1    
    if j < size2:
        while j < size2:
            if arr2[j] != union_arr[-1]:
                union_arr.append(arr2[j])
            j += 1   

    print(union_arr[1:])




arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

union_arr = list(set().union(arr1,arr2))

union(arr1, arr2)

