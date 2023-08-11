class Solution:
    # O(n) time and O(1) space
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        maximum = float("-inf")
        while left < right:
            capacity = getContainerCapacity(left, right, height)

            if height[right] > height[left]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1
            
            maximum = max(maximum, capacity)
        return maximum
    

def getContainerCapacity(start, end, height):
    return (end - start) * min(height[start], height[end])