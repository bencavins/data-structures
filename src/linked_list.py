class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def add_back(self, value):
        new_node = Node(value)
        if self.head is None:  # list is empty
            self.add_front(value)
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
    
    def delete_front(self):
        if self.head is not None:
            self.head = self.head.next
    
    def delete_back(self):
        curr_node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while curr_node.next.next is not None:
                curr_node = curr_node.next
            curr_node.next = None
    
    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value + ' -> ', end='')
            curr_node = curr_node.next
        print()



if __name__ == '__main__':
    ll = LinkedList()
    ll.add_front('a')
    # ll.print_list()
    ll.add_front('b')
    # ll.print_list()
    ll.add_front('c')
    ll.print_list()
    ll.delete_back()
    ll.print_list()
    ll.delete_back()
    ll.print_list()
    ll.delete_back()
    ll.print_list()



