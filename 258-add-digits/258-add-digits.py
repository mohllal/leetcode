class Solution:
    # O(1) time and O(1) space
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9

        return num % 9