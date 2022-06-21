class Solution:
    # O(1) time and O(1) space
    def calcPositiveRoot(self, a, b, c):
        
        d = pow(b, 2) - (4 * a * c)
        sqrt_val = math.sqrt(abs(d))

        root = (-b + sqrt_val) / (2 * a)
        return int(root)

    def arrangeCoins(self, s: int) -> int:
        return self.calcPositiveRoot(1, 1, -2 * s)