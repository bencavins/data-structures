from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f"<Node {self.value}>"


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def print_dfs(self):
        """In order"""
        def traverse(root):
            if root.left:
                traverse(root.left)
            print(root.value)
            # if root.right:
            # traverse(root.right)
        traverse(self.root)
        
    def print_bfs(self):
        q = Queue()
        q.enqueue(self.root)
        while q._data.head is not None:  # while q is not empty
            curr = q.dequeue()
            print(curr.value)
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)
    

t = BinarySearchTree()
t.root = Node(5)
t.root.left = Node(3)
t.root.right = Node(7)
t.root.left.left = Node(2)
t.root.left.right = Node(4)
t.root.right.right = Node(8)
t.root.right.left = Node(6)
t.root.left.left.left = Node(1)