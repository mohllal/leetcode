class Solution:
    # O(n) time and O(1) space
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = start = tank = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
            
        if total >= 0:
            return start
        else:
            return -1
