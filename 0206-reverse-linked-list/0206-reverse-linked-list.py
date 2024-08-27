class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) time and O(1) space
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current = head
        
        while current is not None:
            next_node = current.next
            
            current.next = prev_node
            prev_node = current
    
            current = next_node
        
        return prev_node