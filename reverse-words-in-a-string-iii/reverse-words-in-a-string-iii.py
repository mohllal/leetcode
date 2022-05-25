class Solution:
    # O(n) time and O(1) space
    def reverseInPlace(self, s: List[chr], i: int, j: int) -> None:
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    # O(n ^ 2) time and O(1) space - exculding space for coverting string into mutable type
    def reverseWords(self, s: str) -> str:
        # covert string into array (mutable type)
        strAsArray = list(s)
        
        i = 0
        j = 0
        while i < len(strAsArray):
            if j < len(strAsArray) and strAsArray[j] != ' ':
                j += 1
            else:
                self.reverseInPlace(strAsArray, i, j - 1)
                j += 1
                i = j

        return ''.join(strAsArray)