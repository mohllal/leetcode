class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) time and O(1) space
    def getNodeAtIndex(self, index: int) -> LinkedListNode | None:
        node = self.head
        currentIndex = 0

        while node is not None and currentIndex != index:
            node = node.next
            currentIndex += 1
        
        return node

    # O(n) time and O(1) space
    def get(self, index: int) -> int:
        node = self.getNodeAtIndex(index)
    
        return node.val if node is not None else -1

    # O(1) time and O(1) space
    def addAtHead(self, val: int) -> None:
        node = LinkedListNode(val)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # O(1) time and O(1) space
    def addAtTail(self, val: int) -> None:
        node = LinkedListNode(val)
        
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    # O(n) time and O(1) space
    def addAtIndex(self, index: int, val: int) -> None:
        length = self.length()
        
        if index == 0:
            self.addAtHead(val)

        elif index == length:
            self.addAtTail(val)

        elif index < length:
            nodeAtIndex = self.getNodeAtIndex(index)

            node = LinkedListNode(val)

            node.prev = nodeAtIndex.prev
            node.next = nodeAtIndex

            nodeAtIndex.prev.next = node
            nodeAtIndex.prev = node

    # O(n) time and O(1) space
    def deleteAtIndex(self, index: int) -> None:
        length = self.length()
        
        if index < length:
            nodeAtIndex = self.getNodeAtIndex(index)

            if nodeAtIndex == self.head:
                self.head = self.head.next

            if nodeAtIndex == self.tail:
                self.tail = self.tail.prev

            if nodeAtIndex.prev is not None:
                nodeAtIndex.prev.next = nodeAtIndex.next

            if nodeAtIndex.next is not None:
                nodeAtIndex.next.prev = nodeAtIndex.prev

    # O(n) time and O(1) space
    def length(self) -> int:
        length = 0
        node = self.head
        
        while node is not None:
            node = node.next
            length += 1
        return length

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)