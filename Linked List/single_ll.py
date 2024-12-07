class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            cur_pos = self.head
            while cur_pos.next is not None:
                cur_pos = cur_pos.next
            cur_pos.next = new_node

    def insert_at_next_pos(self, data1, data2):
        new_node = Node(data2)
        if self.head is None:
            print("Element not found. List is empty")
        else:
            cur_pos = self.head
            while cur_pos:
                if cur_pos.data == data1:
                    new_node.next = cur_pos.next
                    cur_pos.next = new_node
                    break
                cur_pos = cur_pos.next
            if cur_pos is None:
                print("Element not found")

    def update_node(self, data1, data2):
        new_node = Node(data2)
        if self.head is None:
            print("Element not found. List is empty")
        else:
            cur_pos = self.head
            while cur_pos:
                if cur_pos.data == data1:
                    cur_pos.data = data2
                    break
                cur_pos = cur_pos.next
            if cur_pos is None:
                print("Element not found")

    # deleting nodes from linked list     
    def delete_from_begn(self):
        if self.head == None:
            return
        
        print("Element deleted is ", self.head.data)
        self.head = self.head.next

    def delete_from_end(self):
        cur_node = self.head
        if cur_node is None:
            return
        
        while cur_node.next.next:
            cur_node = cur_node.next

        cur_node.next = None

    def delete_node_with_data(self, data):
        if self.head is None:
            return
        else:
            cur_pos = self.head
            while cur_pos:
                if cur_pos.next.data == data:
                    print("Element deleted is ", data)
                    cur_pos.next = cur_pos.next.next
                    break
                cur_pos = cur_pos.next
            if cur_pos is None:
                print("Element not found")

    def print_list(self):
        cur_pos = self.head
        while cur_pos is not None:
            print(cur_pos.data, end="-->")
            cur_pos = cur_pos.next

        print()

    def create_ll_from_arr(self, arr):
        for ele in arr:
            #dll.insertAtEnd(ele)
            self.insert_at_end(ele)


ll = Linked_List()

# ll.insert_at_beginning(11)
# ll.insert_at_beginning(2)
# ll.insert_at_end(9)
# ll.insert_at_end(87)
# ll.insert_at_next_pos(9, 17)
# ll.insert_at_next_pos(87, 3)
# ll.update_node(11, 22)
# ll.update_node(2, 5)
# ll.print_list()
# ll.delete_from_begn()
# ll.print_list()
# ll.delete_from_end()
# ll.print_list()
# ll.delete_node_with_data(17)
# ll.print_list()
