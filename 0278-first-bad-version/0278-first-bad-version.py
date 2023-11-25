# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def firstBadVersionHelper(start, end):
            if start > end:
                return float('inf')
        
            mid = (start + end) // 2

            if isBadVersion(mid):
                return min(mid, firstBadVersionHelper(start, mid - 1))
            else:
                return firstBadVersionHelper(mid + 1, end)
            
        return firstBadVersionHelper(1, n)