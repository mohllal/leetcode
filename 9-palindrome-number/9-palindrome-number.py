class Solution:
    def isPalindromeNaive(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False;
        
        xStr = str(x);
        xStrReversed = xStr[::-1];

        return xStr == xStrReversed;
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False;

        lastHalfRevertedNumber = 0;

        while x > lastHalfRevertedNumber:
            lastHalfRevertedNumber = lastHalfRevertedNumber * 10 + (x % 10);
            x //= 10;

        return x == lastHalfRevertedNumber or x == lastHalfRevertedNumber//10;