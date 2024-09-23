def pascal_element(pos, pascal_dict):
    """Beautiful dp implementation of pascal element"""
    if (pos[0],pos[1]) in pascal_dict:
        return pascal_dict[(pos[0], pos[1])]
    elif pos[1] == 0 or pos[1] == pos[0]:
        if (pos[0],pos[1]) not in pascal_dict:
            pascal_dict[(pos[0],pos[1])] = 1
        return pascal_dict[(pos[0],pos[1])] 
    else:
        first_num = pascal_element([pos[0]-1, pos[1]-1],pascal_dict)
        second_num = pascal_element([pos[0]-1, pos[1]],pascal_dict)
        pascal_dict[(pos[0], pos[1])] = first_num + second_num
        return first_num + second_num
        # if (pos[0]-1, pos[1]-1) not in pascal_dict:
        #     pascal_element([pos[0]-1, pos[1]-1])
        # return pascal_dict[(pos[0]-1, pos[1]-1)] + pascal_dict[(pos[0]-1,pos[1])]

pascal_dict = {
        (0,0): 1,
        (1,0): 1,
        (1,1): 1
    }    
print(pascal_element([5,2], pascal_dict))