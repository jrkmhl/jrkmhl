class Node:
    def __init__(self, data, min_val):
        self.data: int = data
        self.min_val: int = min_val


class MinStack:

    def __init__(self):
        self._data: list[Node] = []

    def push(self, val: int) -> None:
        if len(self._data) > 0:
            # get top
            top_node = self._data[-1]
            self._data.append(Node(val, min(val, top_node.min_val)))
        else:
            self._data.append(Node(val, val))

    def pop(self) -> None:
        if len(self._data) > 0:
            self._data.pop()

    def top(self) -> int:
        if len(self._data) > 0:
            return self._data[-1].data

    def getMin(self) -> int:
        if not self._data:
            return self._data[-1].min_val


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
