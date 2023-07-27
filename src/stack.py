# LIFO (Last in, First out)

class Stack:
    def __init__(self):
        self._data = [] # back of array is top of stack

    # O(1)
    def push(self, value):
        self._data.append(value)

    # O(1)
    def pop(self):
        return self._data.pop()
