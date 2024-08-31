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
        
            while fast is not None and fast.next is not None:
                # skip self cycles (one-node length cycle)
                if slow == slow.next or fast == fast.next or fast.next == fast.next.next:
                    break
                
                # skip cycles with mixed directions
                if not (slow.direction == fast.direction == fast.next.direction):
                    break

                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True
            
            return False
        
        nodes = []
        for i in range(len(nums)):
            direction = True if nums[i] >= 0 else False
            nodes.append(ListNode(i, direction))

        for i in range(len(nodes)):
            current_node = nodes[i]
            
            next_node_idx = (i + nums[i]) % len(nums)
            next_node = nodes[next_node_idx]

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

        # O(n) time and O(1) space
        def hasCycleWithSameDirection(nums: List[int], index: int) -> bool:
            slow = index
            fast = index

            while True:
                slow_direction = getDirection(nums, slow)
                slow_next = getNextIndex(nums, slow)
                
                fast_direction = getDirection(nums, fast)
                fast_next = getNextIndex(nums, fast)
                fast_next_direction = getDirection(nums, fast_next)
                fast_next_next = getNextIndex(nums, fast_next)
                
                # skip self cycles (one-node length cycle)
                if slow == slow_next or fast == fast_next or fast_next == fast_next_next:
                    break
                
                # skip cycles with mixed directions
                if not (slow_direction == fast_direction == fast_next_direction):
                    break
        
                slow = slow_next
                fast = fast_next_next

                if slow == fast:
                    return True
            
            return False
        
        # O(n) time and O(1) space
        def markCycleElementsAsVisited(nums: List[int], index: int) -> None:
            slow = index
            temp = nums[index]
            
            # ensure that we only continue moving through the cycle while the elements
            # we are visiting have the same direction as the starting element
            while nums[slow] * temp > 0:
                next_slow = getNextIndex(nums, slow)
                nums[slow] = 0  # mark as visited
                slow = next_slow

        for i in range(len(nums)):
            # skip visited elements
            if nums[i] == 0:
                continue
            
            if hasCycleWithSameDirection(nums, i):
                return True
            
            markCycleElementsAsVisited(nums, i)
    
        return False
            
    def circularArrayLoop(self, nums: List[int]) -> bool:
        return self.circularArrayLoopLinearTimeAndConstantSpace(nums)