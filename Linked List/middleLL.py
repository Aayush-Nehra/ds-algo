from single_ll import Linked_List, create_ll_from_arr

def middleNode(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr:
        if fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
        else:
            break
        slow_ptr = slow_ptr.next
        
        
    
    if fast_ptr.next == None:
        print(slow_ptr.data)
        return slow_ptr
    else:
        print(slow_ptr.next.data)
        return slow_ptr.next

ll = Linked_List()
a = [1,2,3,4]
create_ll_from_arr(a,ll)

middleNode(ll.head)