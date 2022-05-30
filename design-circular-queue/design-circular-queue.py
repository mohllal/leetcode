class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.capacity = k
        self.size = 0
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.tail + 1 < self.capacity:
            self.tail += 1
        else:
            self.tail = 0

        self.size += 1
        self.queue[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head + 1 < self.capacity:
            self.head += 1
        else:
            self.head = 0

        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()