class Solution:
    # O(n * log n) time and O(n) space
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        expected = sorted(heights)
        
        for i in range(0, len(heights)):
            if heights[i] != expected[i]:
                result += 1

        return result