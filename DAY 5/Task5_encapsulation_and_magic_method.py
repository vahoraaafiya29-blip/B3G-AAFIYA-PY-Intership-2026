class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def  __str__(self):
        return str(self.__items)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s)

s.pop()

print(s)