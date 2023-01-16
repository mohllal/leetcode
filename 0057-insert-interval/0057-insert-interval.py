class Solution:
    # O(n) time and O(n) space
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start = None
        end = None
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                start = i
                break
        
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                end = i

        if start == None:
            return intervals + [newInterval]

        if end == None:
            return [newInterval] + intervals
        
        return (
            intervals[:start] +
            [[min(intervals[start][0], newInterval[0]), max(intervals[end][1], newInterval[1])]] + 
            intervals[end + 1:]
        )
        