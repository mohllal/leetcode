class Solution:
    # O(n^2) time and O(n) space
    def circularArrayLoop(self, nums: List[int]) -> bool:
        class ListNode:
            def __init__(self, value: int, direction: bool):
                self.value = value
                self.direction = direction
                self.next = None
            
            def __repr__(self):
                return f'ListNode(\'{self.value}\', {self.direction})'
        
        # O(n) time and O(1) space
        def hasCycleWithSameDirection(head: Optional[ListNode]) -> bool:
            slow = head
            fast = head
            direction = True
            
            while fast is not None and fast.next is not None:
                direction &= (slow.direction == fast.direction == fast.next.direction)
        
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return direction
            
            return False
        
        nodes = []
        for i in range(len(nums)):
            direction = True if nums[i] >= 0 else False
            nodes.append(ListNode(i, direction))

        for i in range(len(nodes)):
            current_node = nodes[i]
            
            next_node_idx = (i + nums[i]) % len(nums)
            next_node = nodes[next_node_idx]
            
            # omitting cycles with one node length
            if current_node != next_node:
                current_node.next = next_node

        for i in range(len(nodes)):
            if hasCycleWithSameDirection(nodes[i]):
                return True
        
        return False