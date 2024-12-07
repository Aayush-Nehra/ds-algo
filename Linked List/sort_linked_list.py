from single_ll import Linked_List, Node

def sortList(head):
    """Naive solution
    Time Complexity: O(n) + O(nlogn) + O(n)
    Space Complexity: O(n)"""
    if head == None or head.next == None:
        return head
    dataList = []
    cur_node = head

    while cur_node:
        dataList.append(cur_node.data)
        cur_node = cur_node.next

    dataList.sort()
    cur_node = head
    for num in dataList:
        cur_node.data = num
        cur_node = cur_node.next

    return head

def mergeLL(head1, head2):
    """Merge two sorted linked lists"""
    temp1 = head1
    temp2 = head2

    #Base case where we have only one element to merge
    if temp1.next == None and temp2.next == None:
        if temp1.data < temp2.data:
            temp1.next = temp2
            return head1
        else:
            temp2.next = temp1
            return head2

    while temp2 != None:
        if temp1.data < temp2.data and temp1.next != None:
            temp1 = temp1.next
        elif temp1.data < temp2.data:
            break
        else:
            # Swap Data
            temp_data = temp1.data
            temp1.data = temp2.data 
            temp2.data = temp_data

            # Creating new links and shifting nodes
            temp_ptr = temp1.next
            temp1.next = temp2
            temp2 = temp2.next
            temp1.next.next = temp_ptr
            temp1 = temp1.next

    if temp2 != None:
        temp1.next = temp2

    return head1

def findMiddle(head):
    slow_ptr = head
    fast_ptr = head.next

    while fast_ptr!= None and fast_ptr.next != None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr

def simpleMerge(list1, list2):
    dummy_node = Node()
    temp = dummy_node

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
            
        temp = temp.next

    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2


    return dummy_node.next

def sortListMergeSort(head):
    if head == None or head.next == None:
        return head
    middle = findMiddle(head)
    right_head = middle.next
    middle.next = None
    left_list = sortListMergeSort(head)
    right_list = sortListMergeSort(right_head)

    return mergeLL(left_list, right_list)   


# ll = Linked_List()
# a = [-1,5,3,4,0]
# ll.create_ll_from_arr(a)
# # sortList(ll.head)
# ll.print_list()

# Checking the merge functionality
# l_1 = Linked_List()
# l_2 = Linked_List()
# a = [1,4,5]
# b = [2,3,6]
# l_1.create_ll_from_arr(a)
# l_2.create_ll_from_arr(b)

# start_ptr = mergeLL(l_1.head, l_2.head)
# print(start_ptr.data)

# l_1.print_list()

#Merge Sort
ll_ms = Linked_List()
a = [4,2,1,3]
a = [-1,5,3,4,0]
a = [3, 2, 4]
ll_ms.create_ll_from_arr(a)

ll_ms.head = sortListMergeSort(ll_ms.head)

print(ll_ms.head.data)
ll_ms.print_list()