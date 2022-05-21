class Solution:
    # O(n) time and O(1) space
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0

        while j < len(needle) and i + j < len(haystack):
            if haystack[i + j] == needle[j]:
                j += 1
            else:
                i += 1
                j = 0
        
        if len(needle) == 0:
            return 0
        elif j == len(needle):
            return i
        else:
            return -1