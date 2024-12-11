from double_LL import DoubleLinkedList

def removeDuplicates(head):
    temp1 = head
    temp2 = head.next

    while temp2:
        if temp1.data == temp2.data and temp2.next != None:
            temp1.next = temp2.next
            temp2.next.prev = temp1
            temp2 = temp1.next
        elif temp1.data == temp2.data and temp2.next == None: 
            temp1.next = None
            temp2 = temp2.next
        else:
            temp1 = temp2
            temp2 = temp2.next

    return head


# Another approach will be to remove links directly by skipping all the repeated numbers instead of updating a link at a time
dll = DoubleLinkedList()
dll.create_dll_from_arr([1,2,2,3,4,4,4])

removeDuplicates(dll.head)
dll.print_list()