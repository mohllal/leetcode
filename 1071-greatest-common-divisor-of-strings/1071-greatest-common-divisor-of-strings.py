class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longest, shortest = (str2, str1) if len(str1) < len(str2) else (str1, str2)
        
        ans = ''
        curr = ''
        for ch in shortest:
            curr += ch
            
            if len(shortest) % len(curr) != 0 or len(longest) % len(curr) != 0:
                continue
    
            socc = shortest.count(curr)
            locc = longest.count(curr)

            if socc == len(shortest) // len(curr) and locc == len(longest) // len(curr):
                ans = curr
        
        return ans
