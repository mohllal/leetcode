class Solution:
    # O(n^2) time and O(n) space
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prevRow = self.getRow(rowIndex - 1)
        currRow = [1] * (rowIndex + 1)

        for i in range(1, len(currRow) - 1):
            currRow[i] = prevRow[i - 1] + prevRow[i]

        return currRow