class Solution:
    # O(n * log n) time and O(1) space
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # O(n * log n) time and O(1) space - quick sort (in-place)
        points.sort(key=lambda point: point[0])

        minimumArrowShots = 1
        currentStart = points[0][0]
        currentEnd = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] >= currentStart and points[i][0] <= currentEnd:
                currentEnd = min(currentEnd, points[i][1])
                continue
            
            minimumArrowShots += 1
            currentStart = points[i][0]
            currentEnd = points[i][1]
        
        return minimumArrowShots
