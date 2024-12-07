from single_ll import Linked_List

def getIntersectionNode2(headA, headB):
    node_set = set()
    list1 = headA
    list2 = headB

    while list1 != None or list2 != None:
        if list1 is not None:
            if list1 not in node_set:
                node_set.add(list1)
                list1 = list1.next
            else:
                return list1
        if list2 is not None:
            if list2 not in node_set:
                node_set.add(list2)
                list2 = list2.next
            else:
                return list2
            
    return None

def getIntersectionNode(headA, headB):
    list1 = headA
    list2 = headB

    list1_extra_len = 0
    list2_extra_len = 0

    while list1 and list2:
        list1 = list1.next
        list2 = list2.next

    if list1:
        while list1:
            list1_extra_len += 1
            list1 = list1.next
    else:
        while list2:
            list2_extra_len += 1
            list2 = list2.next

    list1 = headA
    list2 = headB

    if list1_extra_len != 0:
        while list1_extra_len != 0:
            list1 = list1.next
            list1_extra_len -= 1
    else:
        while list2_extra_len != 0:
            list2 = list2.next
            list2_extra_len -= 1

    while list1 != list2 and list1 and list2:
        list1 = list1.next
        list2 = list2.next

    if list1 == list2:
        return list1
    else:
        return None
    
ll1 = Linked_List()
ll1.create_ll_from_arr([4,1])

ll2 = Linked_List()
ll2.create_ll_from_arr([5,6,1])

ll3 = Linked_List()
ll3.create_ll_from_arr([8,4,5])

temp1 = ll1.head
while temp1.next != None:
    temp1 = temp1.next

temp1.next = ll3.head

temp1 = ll2.head
while temp1.next != None:
    temp1 = temp1.next
temp1.next = ll3.head

getIntersectionNode(ll1.head, ll2.head)

