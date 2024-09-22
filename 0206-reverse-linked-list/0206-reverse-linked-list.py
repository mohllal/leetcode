class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) time and O(n) space
    def reverseList1(self, current: Optional[ListNode]) -> Optional[ListNode]:
        if current is None or current.next is None:
            return current
        
        reversed_head = self.reverseList1(current.next)

        current.next.next = current
        current.next = None
    
        return reversed_head

    # O(n) time and O(1) space
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        previous_node = None
        
        while current_node is not None:
            next_node = current_node.next
            
            current_node.next = previous_node
            previous_node = current_node
    
            current_node = next_node
        
        return previous_node
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseList1(head)
    
    