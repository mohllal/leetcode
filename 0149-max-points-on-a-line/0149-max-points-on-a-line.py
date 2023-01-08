class Solution:
    # O(1) time and O(1) space
    # line slope: https://www.mathsisfun.com/algebra/line-equation-2points.html
    def calculateNormalizedSlope(self, a, b):
        run = a[0] - b[0]

        if run == 0:
            return (1, 0)
        
        if run < 0:
            a, b = b, a
            run = a[0] - b[0]

        rise = a[1] - b[1]
        _gcd = gcd(abs(rise), run)

        return (
            rise // _gcd,
            run // _gcd
        )
    
    # O(n ^ 2) time and O(n) space
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        maximum = 0
        for i in range(0, len(points) - 1):
            a = tuple(points[i])
            counts: DefaultDict[[int, int], int] = {}

            for j in range(i + 1, len(points)):
                b = tuple(points[j])
                slope = self.calculateNormalizedSlope(a, b)
                
                if slope not in counts:
                    counts[slope] = 2
                else:
                    counts[slope] += 1

            maximum = max(
                maximum,
                max(counts.values()),
            )

        return maximum
