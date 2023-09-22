class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.isPowerOfFourLogFourTimeAndLogFourSpace(n)

    # O(log4(n)) time and O(log4(n)) space
    def isPowerOfFourLogFourTimeAndLogFourSpace(self, n):
        if n <= 0:
            return False
        
        if n == 1:
            return True
    
        if not self.isPowerOfFourLogFourTimeAndLogFourSpace(n // 4):
            return False
        
        return n % 4 == 0
    
    # O(log4(n)) time and O(1) space
    def isPowerOfFourLogFourTimeAndConstantSpace(self, n):
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n = n // 4
        
        return True if n == 1 else False