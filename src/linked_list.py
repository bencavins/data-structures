class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return f"<Node {self.value}>"

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_value):
        if self.head is None:
            new_node = Node(new_value)
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                # move to next node
                curr = curr.next
            # found the last node
            curr.next = Node(new_value)
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            # move to next node in list
            current_node = current_node.next

ll = LinkedList()