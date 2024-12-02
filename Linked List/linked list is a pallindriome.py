from single_ll import Linked_List

def isPallindrome(head):
    if head.next == None:
        return True
    
    data_list = []

    current_node = head
    while current_node:
        data_list.append(current_node.data)
        current_node = current_node.next

    for i in range(len(data_list)//2):
        if data_list[i] != data_list[len(data_list)-1-i]:
            return False
        
    return True

def reverseLinkedList(head):
    if head.next == None:
        return head
    prev_node = None
    cur_node = head

    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node

    #New Head is previous node 
    return prev_node

def isPallindromeOptimal(head):
    if head.next == None:
        return True
    
    second_half_head = None
    slow_ptr = head
    fast_ptr = head

    #Find Middle using tortoise and hare
    while fast_ptr.next and fast_ptr.next.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next 

    second_half_head = reverseLinkedList(slow_ptr.next)
    head1 = second_half_head
    head2 = head
    while head1:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next

    return True



a = [1,2]
ll = Linked_List()
ll.create_ll_from_arr(a)

print(isPallindromeOptimal(ll.head))
