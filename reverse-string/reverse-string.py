class Solution:
    # O(n) time and O(n) space
    def reverseStringRecursive(self, s: List[str], start: int, end: int) -> None:
        if start >= end:
            return

        s[start], s[end] = s[end], s[start]        
        self.reverseStringRecursive(s, start + 1, end - 1)

    # O(n) time and O(1) space
    def reverseStringTwoPointers(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseString(self, s: List[str]) -> None:
        # return self.reverseStringTwoPointers(s)
        return self.reverseStringRecursive(s, 0, len(s) - 1)