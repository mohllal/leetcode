class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0] * 38
        tribonacci[0] = 0
        tribonacci[1] = 1
        tribonacci[2] = 1

        for i in range(n - 2):
            tribonacci[i + 3] = tribonacci[i] + tribonacci[i + 1] + tribonacci[i + 2]

        return tribonacci[n]