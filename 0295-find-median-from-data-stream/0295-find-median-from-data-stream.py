import heapq

class MedianFinder:
    def __init__(self):
        # two heaps: one for smaller half and one for larger half
        self.low = []  # max-heap (inverted to use Python's min-heap as max-heap)
        self.high = [] # min-heap
    
    # O(n * logn) time
    def addNum(self, num: int) -> None:
        # if the new number is smaller than or equal to the maximum of the lower half,
        # push it to the max-heap (low). Otherwise, push it to the min-heap (high).
        if len(self.low) == 0 or -self.low[0] >= num:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        
        # balance the heaps: ensure the size difference is no more than 1
        if len(self.low) > len(self.high) + 1:
            # move the largest element of the lower half to the upper half
            top = -heapq.heappop(self.low)
            heapq.heappush(self.high, top)
        elif len(self.high) > len(self.low):
            # move the smallest element of the upper half to the lower half
            top = heapq.heappop(self.high)
            heapq.heappush(self.low, -top)
    
    # O(1) time
    def findMedian(self) -> float:
        if self.is_empty():
            return None

        # if even number of elements, median is the average of the roots of both heaps
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        
        # if odd number of elements, median is the root of the max heap (low)
        # because max heap (low) will always have one more element than min heap (high)
        return -self.low[0]
    
    # O(1) time
    def is_empty(self) -> bool:
        # check if both heaps are empty (no elements have been added)
        return len(self.low) == 0 and len(self.high) == 0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()