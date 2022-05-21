class Solution:
    # O(log n) time and O(1) space
    def binarySearch(self, low, high, target):
        if high < low:
            return high

        mid = (low + high) // 2
        current = mid * mid

        if current > target:
            return self.binarySearch(low, mid - 1, target)
        elif current < target:
            return self.binarySearch(mid + 1, high, target)
        else:
            return mid

    # O(log n) time and O(1) space
    def mySqrt(self, x: int) -> int:
        roots = 46341 # square root of 2 ^ 31

        return self.binarySearch(0, roots - 1, x)