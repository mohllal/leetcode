class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairsRecursive(self,  head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node = head.next
        head.next = self.swapPairsRecursive(head.next.next)        
        node.next = head

        return node
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPairsRecursive(head)
        