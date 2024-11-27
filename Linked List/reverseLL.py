from single_ll import Linked_List

def reverseLLIterative(head):
    """This solution has a memory overhead lets remove the space complexity"""
    cur_node = head
    a = list()
    if cur_node.next == None:
        return cur_node
    
    while cur_node:
        a.append(cur_node.data)
        cur_node = cur_node.next

    cur_node = head

    for i in range(len(a)-1,-1,-1):
        cur_node.data = a[i]
        cur_node = cur_node.next

def reverseLLIterative2(head):
    """This solution doesnt have memory overhead"""
    cur_node = head
    if cur_node == None:
        return head
    
    # Initial value
    prev_node = None
    next_node = cur_node.next

    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node

    head = prev_node
    return prev_node

def reverseLLRecursive(head):
    # Base case. LL contains 0 or 1 elements
    if head == None or head.next == None:
        return head
    
    new_head = reverseLLRecursive(head.next)
    front = head.next
    front.next = head
    head.next = None

    return new_head


a = [1,2,3]
ll = Linked_List()
ll.create_ll_from_arr(a)
ll.print_list()
reverseLLIterative2(ll.head)
ll.print_list()