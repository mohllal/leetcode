# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) time and O(1) space
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            # cycle detected
            if slow == fast:
                # Floyd's cycle detection algorithm
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None