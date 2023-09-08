class Solution:
    # O(n) time and O(n) space
    def divisorSubstrings(self, num: int, k: int) -> int:
        digits = list(str(num))
        
        current = ""
        result = 0
        for i in range(0, len(digits)):
            current += digits[i]
            
            if i >= k - 1:
                divisor = int(current)
                if divisor != 0 and num % divisor == 0:
                    result += 1
                current = current[1:]

        return result
                    
            
        