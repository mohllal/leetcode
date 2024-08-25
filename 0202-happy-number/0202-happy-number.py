class Solution:
    # O(1) time and O(1) space
    # the maximum number of digits `d` is 10 (because 2^31 - 1 = 2,147,483,647, which has 10 digits)
    def sumOfSquares(self, n: int) -> int:
        total = 0

        while n > 0:
            total += (n % 10) ** 2
            n = n // 10

        return total

    def isHappy(self, n: int) -> bool:
        squares = set()
        last_sum = self.sumOfSquares(n)
        
        while last_sum != 1:
            if last_sum in squares:
                return False
            
            squares.add(last_sum)
            last_sum = self.sumOfSquares(last_sum)
        
        return True