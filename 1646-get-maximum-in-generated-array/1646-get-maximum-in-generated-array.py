class Solution:
    # O(n) time and O(n) space
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        maximums = [0] * (n + 1)
        maximums[0] = 0
        maximums[1] = 1
        
        maximum = 1
        for i in range(2, n + 1):
            maximums[i] = maximums[i // 2] if i % 2 == 0 else maximums[i // 2] + maximums[(i // 2) + 1]
            maximum = max(maximum, maximums[i])

        return maximum