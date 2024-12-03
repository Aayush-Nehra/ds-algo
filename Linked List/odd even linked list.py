from single_ll import Linked_List

def oddEvenList(head):
    if head == None or head.next == None or head.next.next == None:
        return
    oddEndPtr = head
    evenEndPrt = head.next
    curElement = head.next.next

    while curElement:
        evenEndPrt.next = curElement.next
        curElement.next = oddEndPtr.next 
        oddEndPtr.next = curElement

        # Reset the pointers
        oddEndPtr = oddEndPtr.next 
        evenEndPrt = evenEndPrt.next
        if evenEndPrt == None:
            break
        curElement = evenEndPrt.next



ll = Linked_List()
a = [1,2, 3, 4,5, 6,7]
ll.create_ll_from_arr(a)
oddEvenList(ll.head)

ll.print_list()

