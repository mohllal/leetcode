from sortedcontainers import SortedSet

class SummaryRanges:
    def __init__(self):
        self.values = SortedSet()

    def addNum(self, value: int) -> None:
        self.values.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        if len(self.values) == 0:
            return intervals

        left = self.values[0]
        right = self.values[0]
        for i in range(1, len(self.values)):
            if self.values[i] == right + 1:
                right = self.values[i]
            else:
                intervals.append([left, right])
                left = right = self.values[i]
        
        intervals.append([left, right])
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()