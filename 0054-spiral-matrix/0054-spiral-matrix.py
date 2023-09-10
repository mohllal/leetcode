class Solution:
    # O(n) time and O(n) space - n is the total number of elements
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        rows = len(matrix)
        columns = len(matrix[0])

        rStart, rEnd = 0, rows - 1
        cStart, cEnd = 0, columns - 1
        while rStart <= rEnd and cStart <= cEnd:
            self.rectangleTraverse(rStart, rEnd, cStart, cEnd, matrix, output)

            rStart += 1
            rEnd -= 1

            cStart += 1
            cEnd -= 1

        return output
    
    def rectangleTraverse(self, rStart, rEnd, cStart, cEnd, matrix, output):
        for column in range(cStart, cEnd + 1):
            output.append(matrix[rStart][column])

        for row in range(rStart + 1, rEnd + 1):
            output.append(matrix[row][cEnd])

        if rEnd != rStart:
            for column in reversed(range(cStart, cEnd)):
                output.append(matrix[rEnd][column])

        if cEnd != cStart:
            for row in reversed(range(rStart + 1, rEnd)):
                output.append(matrix[row][cStart])