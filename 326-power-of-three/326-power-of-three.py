class Solution:
    # O(log3 n) time and O(log3 n) space
    def isPowerOfThreeLogThreeTimeAndLogThreeSpaceRecursive(self, n: int) -> bool:
        if n < 3:
            return False
        if n == 3:
            return True

        return self.isPowerOfThreeRecursive(n / 3)

    # O(log3 n) time and O(1) space
    def isPowerOfThreeLogThreeTimeAndConstantSpaceIterative(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n % 3 == 0:
            n /= 3
        
        return True if n == 1 else False

    def isPowerOfThree(self, n: int) -> bool:
        return self.isPowerOfThreeLogThreeTimeAndConstantSpaceIterative(n)
        