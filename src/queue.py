# First in, first out (FIFO)

from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, value):
        self.data.add_back(value)

    def dequeue(self):
        return self.data.delete_front()
    
    def is_empty(self):
        return self.data.head is None
    
    def print(self):
        self.data.print_list()


if __name__ == '__main__':
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.print()
    q.dequeue()
    q.print()