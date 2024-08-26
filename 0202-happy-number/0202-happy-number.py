class Solution:
    # O(log n) time and O(1) space
    # d (number of digits) = (Log(10) n) + 1 ~ O(log n)
    def sumOfSquares(self, n: int) -> int:
        total = 0

        while n > 0:
            total += (n % 10) ** 2
            n = n // 10

        return total

    # O(k * log n) time and O(k) space
    # k is the number of iterations required to determine whether the number is happy or not.
    def isHappy1(self, n: int) -> bool:
        squares = set()
        last_sum = self.sumOfSquares(n)
        
        while last_sum != 1:
            if last_sum in squares:
                return False
            
            squares.add(last_sum)
            last_sum = self.sumOfSquares(last_sum)
        
        return True
    
    # O(k * log n) time and O(1) space
    # k is the number of iterations required to determine whether the number is happy or not.
    def isHappy2(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)
        
        while fast != slow:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        
        return True if fast == 1 else False
    
    def isHappy(self, n: int) -> bool:
        return self.isHappy2(n)