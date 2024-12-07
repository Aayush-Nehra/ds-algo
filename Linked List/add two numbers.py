from single_ll import Linked_List, Node

def addTwoNumbers(l1, l2):
    ans_head = Node()
    temp = ans_head
    carry = 0
    while l1 != None or l2!= None:
        new_node = Node()
        if l1 == None:
            l1_val = 0
        else:
            l1_val = l1.data
            l1 = l1.next

        if l2 == None:
            l2_val = 0
        else:
            l2_val = l2.data
            l2 = l2.next

        total = l1_val + l2_val + carry

        if total >= 10:
            carry = 1
            total = total - 10
            new_node.data = total
            temp.next = new_node
            temp = new_node
        else:
            carry = 0
            new_node.data = total
            temp.next = new_node
            temp = new_node

    if carry == 1:
        new_node = Node(1)
        temp.next = new_node

    return ans_head.next

l1 = Linked_List()
l2 = Linked_List()

# a = [2,4,3]
# a = [0]
a = [9,9,9,9,9,9,9]
l1.create_ll_from_arr(a)

# b = [5,6,4]
# b = [0]
b = [9,9,9,9]
l2.create_ll_from_arr(b)

l3 = Linked_List()
l3.head = addTwoNumbers(l1.head, l2.head)

l3.print_list()