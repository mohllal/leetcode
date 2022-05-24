class Solution:
    # O(n) time and O(1) space
    def reverseStringIterative(self, s: List[str]) -> None:
        mid = len(s) // 2
        length = len(s) - 1
        
        for i in range(0, mid):
            s[i], s[length - i] = s[length - i], s[i]
            
    # O(n) time and O(1) space
    def reverseStringTwoPointers(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseString(self, s: List[str]) -> None:
        return self.reverseStringTwoPointers(s)