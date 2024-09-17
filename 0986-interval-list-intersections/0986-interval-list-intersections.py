class Solution:
    # O(n + m) time and O(n + m) space
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def getIntersection(interval_1: List[int], interval_2: List[int]) -> Optional[Tuple[int, int]]:
            first_started = interval_1
            second_started = interval_2

            if second_started[0] < first_started[0]:
                first_started, second_started = second_started, first_started
                
            if second_started[0] <= first_started[1]:        
                return (
                    max(first_started[0], second_started[0]),
                    min(first_started[1], second_started[1])
                )
            
            return None

        intersections = []

        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            interval1 = firstList[i]
            interval2 = secondList[j]

            intersection = getIntersection(interval1, interval2)
            if intersection:
                intersections.append(intersection)
            
            # move next from the interval which finishes first
            if interval1[1] < interval2[1]:
                i += 1
            elif interval2[1] < interval1[1]:
                j += 1
            else:
                i += 1
                j += 1

        return intersections