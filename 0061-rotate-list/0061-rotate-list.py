class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) time and O(1) space
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # count the length of the list and find the tail
        length = 1
        tail = head
        while tail.next is not None:
            length += 1
            tail = tail.next
            
        # if the number of rotations will revert back the linked list to its original form
        k = k % length
        if k == 0:
            return head
        
        # find the new head after rotation
        # new head will be at (length - k)th node, and new tail will be just before it
        new_tail_position = length - k
        new_tail = head
        for _ in range(new_tail_position - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None # break the link between the old tail and the new head
        tail.next = head  # connect the old tail of the list to the old head
        
        return new_head