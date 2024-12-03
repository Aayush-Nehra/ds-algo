from single_ll import Linked_List

def removeNthFromEnd(head, n):
    lenLinkedList = 0
    temp = head

    while temp:
        lenLinkedList += 1
        temp = temp.next 

    # Node to be removed
    k = lenLinkedList - n 
    if k == 0:
        head = head.next
        return head 
    print(k)
    temp = head
    for i in range(1,k):
        temp = temp.next

    print(temp.data)

    if temp.next.next != None:
        temp.next = temp.next.next
    else:
        temp.next = None

    return head
    

ll = Linked_List()
a = [1,2]
ll.create_ll_from_arr(a)

removeNthFromEnd(ll.head, 2)
ll.print_list()