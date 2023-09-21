class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersFasterLinearTimeAndLinearSpace(l1, l2)

    # O(n+m) time and O(n+m) space
    def addTwoNumbersFasterLinearTimeAndLinearSpace(self, l1, l2):
        return self.sumLists(l1, l2)

    def sumLists(self, l1, l2, carry=0):
        if l1 is None and l2 is None and carry == 0:
            return None
        
        l1Val = l1.val if l1 is not None else 0
        l2Val = l2.val if l2 is not None else 0
        lSum = l1Val + l2Val + carry
        
        l1Next = l1.next if l1 is not None else None
        l2Next = l2.next if l2 is not None else None
    
        node = ListNode(lSum % 10)
        node.next = self.sumLists(l1Next, l2Next, lSum // 10)
    
        return node
        
    # O(n+m) time and O(n+m) space
    def addTwoNumbersLinearTimeAndLinearSpace(self, l1, l2):
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