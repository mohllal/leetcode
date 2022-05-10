def binarySearch(low, high, target):
    if high < low:
        return high

    mid = (low + high) // 2
    current = mid * mid

    if current > target:
        return binarySearch(low, mid - 1, target)
    elif current < target:
        return binarySearch(mid + 1, high, target)
    else:
        return mid
    
class Solution:
    def mySqrt(self, x: int) -> int:
        roots = 46341 # square root of 2^31

        return binarySearch(0, roots - 1, x)