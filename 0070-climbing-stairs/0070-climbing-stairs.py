class Solution:
    # O(n) time and O(n) space
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n + 1)
        steps[0] = 1
        steps[1] = 2

        for i in range(n - 2):
            steps[i + 2] = steps[i + 1] + steps[i]

        return steps[n - 1]