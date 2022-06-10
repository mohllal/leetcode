class Solution:
    # O(n) time and O(n) space
    def numSquaresLinearTimeAndLinearSpace(self, n: int) -> int:
        squares = []
        for i in range(1, int(sqrt(n)) + 1):
            squares.append(i**2)

        distance = 1
        queue = {n}

        while queue:
            currentLevel = set()
            for node in queue:
                for square in squares:
                    if node == square:
                        return distance
                    if node < square:
                        break
                    currentLevel.add(node - square)
            distance += 1
            queue = currentLevel

    def numSquares(self, n: int) -> int:
        return self.numSquaresLinearTimeAndLinearSpace(n)
