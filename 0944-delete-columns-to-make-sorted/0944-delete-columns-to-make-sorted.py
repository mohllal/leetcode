class Solution:
    # O(n * m) time and O(1) space - m being the string length
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        n = len(strs)
        z = len(strs[0])

        for i in range(z):
            for j in range(n - 1):
                if strs[j][i] > strs[j + 1][i]:
                    result += 1
                    break

        return result