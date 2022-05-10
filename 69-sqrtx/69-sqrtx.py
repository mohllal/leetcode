def binarySearch(low, high, target):
    if high < low:
        return (low, False)

    mid = (low + high) // 2
    current = mid * mid

    if current > target:
        return binarySearch(low, mid - 1, target)
    elif current < target:
        return binarySearch(mid + 1, high, target)
    else:
        return (mid, True)
    
class Solution:
    def mySqrt(self, x: int) -> int:
        roots = 46341 # square root of 2^31

        (index, match) = binarySearch(0, roots - 1, x)
        return index - 1 if (not match) else index