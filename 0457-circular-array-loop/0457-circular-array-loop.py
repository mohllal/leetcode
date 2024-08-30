class Solution:
    # O(n^2) time and O(n) space
    def circularArrayLoopQuadraticTimeAndLinearSpace(self, nums: List[int]) -> bool:
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
            
            # omitting self cycles (one node length cycle)
            if current_node != next_node:
                current_node.next = next_node

        for i in range(len(nodes)):
            if hasCycleWithSameDirection(nodes[i]):
                return True
        
        return False
    
    # O(n) time and O(1) space
    def circularArrayLoopLinearTimeAndConstantSpace(self, nums: List[int]) -> bool:
        # O(1) time and O(1) space
        def getNextIndex(nums: List[int], index: int) -> int:
            return (index + nums[index]) % len(nums)
        
        # O(1) time and O(1) space
        def getDirection(nums: List[int], index: int) -> bool:
            return nums[index] > 0
        
        # O(1) time and O(1) space
        def isSelfCycle(nums: List[int], index: int) -> bool:
            return index == getNextIndex(nums, index)
            
        # O(n) time and O(1) space
        def hasCycleWithSameDirection(nums: List[int], index: int) -> bool:
            slow = index
            fast = index
            direction = True
            
            while True:
                slow_direction = getDirection(nums, slow)
                slow_next = getNextIndex(nums, slow)
                
                fast_direction = getDirection(nums, fast)
                fast_next = getNextIndex(nums, fast)
                fast_next_direction = getDirection(nums, fast_next)
                fast_next_next = getNextIndex(nums, fast_next)
                
                # omitting self cycles (one node length cycle)
                if slow == slow_next or fast == fast_next or fast_next == fast_next_next:
                    break
        
                direction &= (slow_direction == fast_direction == fast_next_direction)
        
                slow = slow_next
                fast = fast_next_next

                if slow == fast:
                    return direction
            
            return False
        
        for i in range(len(nums)):
            if hasCycleWithSameDirection(nums, i):
                return True

        return False
            
    def circularArrayLoop(self, nums: List[int]) -> bool:
        return self.circularArrayLoopLinearTimeAndConstantSpace(nums)