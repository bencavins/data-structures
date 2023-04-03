# Last in, first out (LIFO)

class Stack:
    def __init__(self):
        # back of list is top of stack
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    print(s.data)
    s.pop()
    print(s.data)
