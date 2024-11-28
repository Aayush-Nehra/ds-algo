from single_ll import Linked_List

def hasCycle(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            slow_ptr = head
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            return slow_ptr
        
    return None