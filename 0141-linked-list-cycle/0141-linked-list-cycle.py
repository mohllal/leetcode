class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(n) time and O(1) space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
    
        
        return False