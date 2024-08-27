class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # O(n) time and O(1) space
        def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
            prev_node = None
            current = node
            
            while current is not None:
                next_node = current.next
                
                current.next = prev_node
                prev_node = current
                
                current = next_node
                
            return prev_node
        
        # O(n) time and O(1) space
        def getMiddleNode(node: Optional[ListNode]) -> Optional[ListNode]:
            slow = node
            fast = node
            
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
            return slow
        
        second_half = getMiddleNode(head)
        reversed_second_half = reverseList(second_half)
      
        pointer1 = head
        pointer2 = reversed_second_half
        while pointer1 is not None and pointer2 is not None:
            pointer1_next = pointer1.next
            pointer2_next = pointer2.next
            
            # preventing cycle
            if pointer1.next != pointer2:
                pointer1.next = pointer2
                pointer2.next = pointer1_next       
          
            pointer1 = pointer1_next
            pointer2 = pointer2_next
        
        return head