class Solution:
    # O(log3(n)) time and O(log3(n)) space
    def isPowerOfThreeLogThreeTimeAndLogThreeSpace(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
    
        if not self.isPowerOfThreeLogThreeTimeAndLogThreeSpace(n // 3):
            return False
        
        return n % 3 == 0

    # O(log3(n)) time and O(1) space
    def isPowerOfThreeLogThreeTimeAndConstantSpace(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n /= 3
        
        return True if n == 1 else False

    def isPowerOfThree(self, n: int) -> bool:
        return self.isPowerOfThreeLogThreeTimeAndConstantSpace(n)