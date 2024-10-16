import heapq
from collections import defaultdict

# O(1) time
def findMedian(low: List[int], high: List[int], k: int) -> Optional[float]:
    if len(low) == 0 and len(high) == 0:
        return None
    
    if k % 2:
        # if k is odd, the median is the top of low heap
        return float(-low[0])
    else:
        # if k is even, the median is the average of the tops of both heaps
        return (-low[0] + high[0]) / 2.0

class Solution:
    # O(n * logk) time and O(n) space
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) == 0 or k == 0:
            return []

        low = [] # max-heap to store the lower half of numbers (invert values for Python's min-heap)
        high = [] # min-heap to store the upper half of numbers
        to_remove = defaultdict(int) # tracks elements that need to be removed from heaps
        medians = []

        # initialize the heaps with the first k elements
        for i in range(k):
            heappush(low, -nums[i])
            heappush(high, -heappop(low))

            # balance the heaps if high has more elements
            if len(high) > len(low):
                heappush(low, -heappop(high))

        # calculate and store the median for the first window
        median = findMedian(low, high, k)
        medians.append(median)

        # iterate through the array starting from the k-th element
        for i in range(k, len(nums)):
            # mark the number that is sliding out of the window for removal
            out_num = nums[i - k]
            to_remove[out_num] += 1

            # determine which heap the outgoing number belongs to by comparing with the current median
            # if the outgoing number is less than or equal to the median, it was part of the low (max-heap)
            # otherwise, it was part of the high (min-heap)
            balance = -1 if out_num <= median else 1
        
            # add the new incoming number to the appropriate heap based on its value relative to the median
            if nums[i] <= median:
                balance += 1
                heappush(low, -nums[i])
            else:
                balance -= 1
                heappush(high, nums[i])
        
            # rebalance the heaps to maintain size properties after addition
            if balance < 0:
                # if high heap has more elements, move the smallest from high to low to balance
                # when we remove an element from low (max-heap) and then add a new one to high (min-heap)
                heappush(low, -heappop(high))
            elif balance > 0:
                # if low heap has more elements, move the largest from low to high to balance
                # when we remove an element from high (min-heap) and then add a new one to low (max-heap)
                heappush(high, -heappop(low))

            # remove elements from low heap that are marked for removal
            while low and to_remove[-low[0]] > 0:
                to_remove[-low[0]] -= 1
                heappop(low)
            
            # remove elements from high heap that are marked for removal
            while high and to_remove[high[0]] > 0:
                to_remove[high[0]] -= 1
                heappop(high)
            
            # calculate and store the current median after rebalancing and removals
            median = findMedian(low, high, k)
            medians.append(median)
        
        return medians