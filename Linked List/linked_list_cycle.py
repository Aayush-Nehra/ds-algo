from single_ll import Linked_List

def hasCycle(head):
    slow_ptr = head
    fast_ptr = head

    while slow_ptr and fast_ptr and fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True
        
    return False

def detectCycle(head):
    cur_node = head
    posDict = {}
    pos = 0
    while cur_node.next:
        if cur_node in posDict:
            return posDict[cur_node]
        else:
            posDict[cur_node] = pos
            pos += 1
            cur_node = cur_node.next
    
    return -1

#Creating data
ll = Linked_List()
# ll.create_ll_from_arr([1,2,3,4,5])
ll.create_ll_from_arr([1,2])

tail = None
cur_node = ll.head
while cur_node.next:
    cur_node = cur_node.next

# print(cur_node.data)
cur_node.next = ll.head.next
# ll.insert_at_beginning(1)

print(detectCycle(ll.head))