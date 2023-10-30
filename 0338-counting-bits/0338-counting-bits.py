class Solution:
    # O(n) time and O(n) space
    def countBits(self, n: int) -> List[int]:
        bits = [-1] * (n + 1)
        bits[0] = 0
        lastPowerOfTwo = 0

        for i in range(1, n + 1):
            if self.isPowerOfTwo(i):
                bits[i] = 1
                lastPowerOfTwo = i
            else:
                bits[i] = bits[lastPowerOfTwo] + bits[i - lastPowerOfTwo]
                
        return bits

    def isPowerOfTwo(self, num):
        return num > 0 and (num & (num - 1)) == 0