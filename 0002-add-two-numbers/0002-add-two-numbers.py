class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n+m) time and O(n+m) space
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Number = self.listToNumber(l1)
        l2Number = self.listToNumber(l2)
        
        lSum = l1Number + l2Number
        if lSum == 0:
            return ListNode(0)
    
        return self.numberToList(lSum)
    
    def listToNumber(self, l, p=0):
        if l is None:
            return 0
        
        return l.val * pow(10, p) + self.listToNumber(l.next, p + 1)
    
    def numberToList(self, n):
        if n == 0:
            return None
        
        node = ListNode(n % 10)
        node.next = self.numberToList(n // 10)
        
        return node