class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __eq__(self, other_node):
        return self.value == other_node.value

    def __gt__(self, other_node):
        return self.value > other_node.value

    def __lt__(self, other_node):
        return self.value < other_node.value



class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if root.value > value:
                pass # go left
            else:  # root.value <= value:
                pass # go right
        
    def print_dfs(self):
        def traverse(root):
            if root:
                traverse(root.left)
                print(root.value)
                traverse(root.right)
        traverse(self.root)
    
    def print_bfs(self):
        from queue import Queue
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr_node = q.dequeue()
            print(curr_node.value)
            if curr_node.left:
                q.enqueue(curr_node.left)
            if curr_node.right:
                q.enqueue(curr_node.right)
    
    def validate(self):
        from queue import Queue
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr_node = q.dequeue()
            print(curr_node.value)
            if curr_node.left:
                if curr_node.left.value > curr_node.value:
                    return False
                q.enqueue(curr_node.left)
            if curr_node.right:
                if curr_node.right.value < curr_node.value:
                    return False
                q.enqueue(curr_node.right)
        return True
        



if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(2)

    tree = BinarySearchTree()
    tree.root = root
    print(tree.validate())

