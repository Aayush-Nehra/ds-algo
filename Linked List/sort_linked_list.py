from single_ll import Linked_List

def sortList(head):
    """Naive solution
    Time Complexity: O(n) + O(nlogn) + O(n)
    Space Complexity: O(n)"""
    if head == None or head.next == None:
        return head
    dataList = []
    cur_node = head

    while cur_node:
        dataList.append(cur_node.data)
        cur_node = cur_node.next

    dataList.sort()
    cur_node = head
    for num in dataList:
        cur_node.data = num
        cur_node = cur_node.next

    return head
    
    


ll = Linked_List()
a = [-1,5,3,4,0]
ll.create_ll_from_arr(a)
sortList(ll.head)
ll.print_list()