import heapq

class Solution:
    # O(n * log n) time and O(n) space
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: (trip[1], trip[2]))

        max_capacity = 0
        curr_capacity = 0
        min_heap = [] # min heap which represents all ongoing trips
        for i in range(len(trips)):
            # remove all the trips that have ended
            while len(min_heap) > 0 and trips[i][1] >= min_heap[0][0]:
                curr_capacity -= min_heap[0][1]
                heapq.heappop(min_heap)

            # push end location and capacity for the current trip into the min heap
            curr_capacity += trips[i][0]
            heapq.heappush(min_heap, (trips[i][2], trips[i][0]))

            max_capacity = max(max_capacity, curr_capacity)

        return max_capacity <= capacity