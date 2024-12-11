from double_LL import DoubleLinkedList

def findPairsWithGivenSum(head, target):
    seen_elements = set()
    temp = head
    ans = []
    while temp:
        seen_elements.add(temp.data)
        x = target - temp.data
        if x in seen_elements and x!= temp.data:
            ans.append([x, temp.data])
        temp = temp.next
        
    return ans

dll = DoubleLinkedList()
dll.create_dll_from_arr([1,2,3,5,6,8,9])
target = 7

findPairsWithGivenSum(dll.head, target)
