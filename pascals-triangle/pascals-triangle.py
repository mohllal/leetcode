class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(0, numRows):
            result.append([1] * (i + 1))
        
        for i in range(2, len(result)):
            prev = result[i - 1]
            k = 1
            for j in range(1, len(prev)):
                result[i][k] = result[i - 1][j] + result[i - 1][j - 1]
                k += 1
        return result