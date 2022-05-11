class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted = []

    def push(self, val: int) -> None:
        self.sorted.append(val)
        self.sorted.sort()
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.sorted.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()