from single_ll import Linked_List

def deleteMiddle(head):
    """Time Complexity = O(N) space Complexity = O(1)"""
    """For one pass you may also consider moving fast by two steps and skipping first step of slow"""
    if head == None or head.next == None:
        return None
    if head.next.next == None:
        head.next = None
        return head
    
    slow_ptr = head
    fast_ptr = head

    # Alternate solution
    # fast_ptr = fast_ptr.next.next

    # while fast_ptr.next != None and fast_ptr != None:
    #     slow_ptr = slow_ptr.next 
    #     fast_ptr = fast_ptr.next.next 

    while fast_ptr.next.next is not None and fast_ptr.next.next.next != None:
        slow_ptr = slow_ptr.next 
        fast_ptr = fast_ptr.next.next 

    slow_ptr.next = slow_ptr.next.next 
    return head

def deleteMiddleTwoPass(head):
    if head == None or head.next == None:
        return None
    # Find length of ll
    count_nodes = 0
    cur_node = head

    while cur_node:
        count_nodes += 1
        cur_node = cur_node.next 

    #Find middle position
    middlePos = count_nodes//2

    # Traverse till one before middle
    cur_node = head
    for i in range(middlePos - 1):
        cur_node = cur_node.next

    cur_node.next = cur_node.next.next

    return head



ll = Linked_List()
a = [1,2]
ll.create_ll_from_arr(a)

deleteMiddleTwoPass(ll.head)
ll.print_list()