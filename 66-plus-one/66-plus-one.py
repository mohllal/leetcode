class Solution:
    # O(n) time and O(n) space
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        remaining = 1
        i = len(digits) - 1

        while i >= 0:
            current = digits[i] + remaining
            if current == 10:
                result = [0] + result
                remaining = 1
            else:
                result = [current] + result
                remaining = 0
            i -= 1
        
        if remaining == 1:
            result = [1] + result

        return result