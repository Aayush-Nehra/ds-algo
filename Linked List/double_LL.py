class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Insert
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertInMiddle(self, data, pos):
        cur_pos = 0
        cur_node = self.head
        new_node = Node(data)

        for _ in range(pos):
            cur_node = cur_node.next

        new_node.next = cur_node.next
        new_node.prev = cur_node
        cur_node.next.prev = new_node
        cur_node.next = new_node

    #Reverse a linked list - optimal
    def revDLLOptimal(self):
        """TC - O(n) SC-O(1)"""
        cur_node = self.head
        temp = None
        while cur_node:
            cur_node.prev = cur_node.next
            cur_node.next = temp
            temp = cur_node
            
            cur_node = cur_node.prev

        self.head = temp


    def print_list(self):
        cur_pos = self.head
        while cur_pos is not None:
            print(cur_pos.data, end="<-->")
            cur_pos = cur_pos.next

        print()

def create_dll_from_arr(arr, dll):
    for ele in arr:
        #dll.insertAtEnd(ele)
        dll.insertAtBeginning(ele)

# Testing
# Creating double linked list 
dll = DoubleLinkedList()

# inserting at end
# dll.insertAtEnd(1)
# dll.insertAtEnd(3)

# arr = [5,7,8,2,4]
# create_dll_from_arr(arr, dll)
# dll.print_list()

# dll.insertInMiddle(6, 3)

#Reverse DLL
arr = [1,2,3,4,5]
create_dll_from_arr(arr, dll)
dll.print_list()

dll.revDLLOptimal()
dll.print_list()

