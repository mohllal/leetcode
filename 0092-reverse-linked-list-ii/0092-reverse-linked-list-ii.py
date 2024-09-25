class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) time and O(1) space
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        node_before_start = None  # this will point to the node just before the 'left' position
        start_node = None         # this will point to the node at the 'left' position
        node_after_end = None     # this will point to the node right after the 'right' position
        end_node = None           # this will point to the node at the 'right' position
        
        current_position = 1
        previous_node = None
        current_node = head
        while current_node is not None:
            next_node = current_node.next

            if current_position == left:
                node_before_start = previous_node # node just before the 'left' position
                start_node = current_node # node at the 'left' position
            elif current_position == right:
                end_node = current_node # node at the 'right' position
                node_after_end = next_node # node just after the 'right' position
            
            # reverse the links between 'left' and 'right' positions
            if current_position >= left and current_position <= right:
                current_node.next = previous_node
            
            # move forward in the list
            previous_node = current_node
            current_node = next_node
            current_position += 1

        # reconnect the reversed portion with the rest of the list
        # node_before_start -> (end_node) -> .. -> (start_node) -> node_after_end

        # if there's a node before the start, link it to the new head of the reversed sublist
        if node_before_start:
            node_before_start.next = end_node
        else:
            head = end_node  # if reversing from the first node, adjust the head to the new start
        
        # link the original start node to the node after the end of the reversed portion
        start_node.next = node_after_end
        
        return head