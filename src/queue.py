from linked_list import LinkedList
# FIFO (first in, first out)

class Queue:
    def __init__(self):
        self._data = LinkedList()

    # O(1)
    def enqueue(self, value):
        self._data.add_back(value)

    # O(1)
    def dequeue(self):
        return self._data.delete_front()
