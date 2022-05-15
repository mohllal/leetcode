# 8 -> 1000, 7 -> 0111 so 1000 & 0111 -> 0000
# 12 -> 1100, 11 -> 1101 so 1100 & 1101 -> 1100

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        isPowerOfTwo = (n != 0 and (n & n - 1) == 0)
        return isPowerOfTwo