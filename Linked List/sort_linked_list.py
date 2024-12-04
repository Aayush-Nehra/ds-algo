from single_ll import Linked_List

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

    while temp1.next != None:
        if temp1.data < temp2.data:
            temp1 = temp1.next
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

def sortListMergeSort(head):
    pass    


# ll = Linked_List()
# a = [-1,5,3,4,0]
# ll.create_ll_from_arr(a)
# # sortList(ll.head)
# ll.print_list()

# Checking the merge functionality

l_1 = Linked_List()
l_2 = Linked_List()
a = [1,4,5]
b = [2,3,6]
l_1.create_ll_from_arr(a)
l_2.create_ll_from_arr(b)

start_ptr = mergeLL(l_1.head, l_2.head)
print(start_ptr.data)

l_1.print_list()