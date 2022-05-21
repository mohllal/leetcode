class Solution:
    # O(n) time and O(1) space
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n &= n - 1
            count += 1

        return count