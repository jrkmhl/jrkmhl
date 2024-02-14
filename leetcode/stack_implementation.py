class Stack:
    def __init__(self):
        # create empty list
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, ele):
        self._data.append(ele)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        return len(self._data) > 0

    def top(self):
        if len(self._data) > 0:
            return self._data[-1]
        else:
            print("Emptry")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

while s.is_empty():
    print(s.pop())

