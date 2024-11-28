def countNodesInLoop(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            count = 1
            slow_ptr = slow_ptr.next
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                count += 1
            return count
        
    return 0