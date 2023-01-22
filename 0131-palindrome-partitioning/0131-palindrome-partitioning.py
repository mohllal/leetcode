class Solution:
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -=1

        return True
    
    def backtrack(self, s, start, parition, result):
        if start >= len(s):
            result.append(parition)
                
        for l in range(len(s) - start):
            if self.isPalindrome(s, start, start + l):
                currentStart = start + l + 1
                currentParition = parition + [s[start:start + l + 1]]
                
                self.backtrack(s, currentStart, currentParition, result)

    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(s, 0, [], result)

        return result
