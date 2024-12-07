from double_LL import DoubleLinkedList, Node

def deleteFromBeginning():
    pass

def deleteAllOccurOfX(head, x):
    if head == None:
        return None
    if head.prev == None and head.next == None:
        if head.data == x:
            return None
    temp = head
    while temp:
        if temp.data == x:
            # Decide delete from beginning middle or end
            # Beginning
            if temp.prev == None:
                temp = temp.next
                temp.prev = None
                head = temp
            elif temp.prev != None and temp.next!= None:
                next_node = temp.next
                temp.prev.next = next_node
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
                temp = next_node
            else:
                prev_node = temp.prev
                temp.prev.next = None
                temp.prev = None
                temp = prev_node
        if temp.data != x:
            temp = temp.next

    return head


dll = DoubleLinkedList()
a = [2,2,18,8,4,2,2,2,2,5,2]
dll.create_dll_from_arr(a)
dll.print_list()
dll.head = deleteAllOccurOfX(dll.head, 2)
dll.print_list()
