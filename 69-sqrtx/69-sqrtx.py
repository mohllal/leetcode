def binarySearch(low, high, squares, target):
    if high < low:
        return (low, False)

    mid = (low + high) // 2
    if squares[mid] > target:
        return binarySearch(low, mid - 1, squares, target)
    elif squares[mid] < target:
        return binarySearch(mid + 1, high, squares, target)
    else:
        return (mid, True)
    
class Solution:
    def mySqrt(self, x: int) -> int:
        roots = 46341 # square root of 2^31
        squares = [0] * roots
        
        for i in range(0, roots):
            squares[i] = i * i

        (index, match) = binarySearch(0, roots - 1, squares, x)
        return index - 1 if (not match) else index