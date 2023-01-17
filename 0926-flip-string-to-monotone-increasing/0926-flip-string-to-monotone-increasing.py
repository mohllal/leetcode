class Solution:
    # O(n) time and O(1) space
    def minFlipsMonoIncr(self, s: str) -> int:
        currentFlips = s.count('0')
        numberOfFlips = currentFlips
        
        for char in s:
            if char == '0':
                currentFlips -= 1
                numberOfFlips = min(numberOfFlips, currentFlips)
            else:
                currentFlips += 1
        
        return numberOfFlips
