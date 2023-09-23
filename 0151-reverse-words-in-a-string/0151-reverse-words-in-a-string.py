class Solution:
    # O(n) time and O(n) space
    def reverseWordsLinearTimeAndLinearSpace(self, s: str) -> str:
        result = ''
        splitted = s.strip().split(' ')
        
        i = len(splitted) - 1
        while i >= 0:
            if splitted[i] != '':
                current = splitted[i] + ' ' if i != 0 else splitted[i]
                result += current
            i -= 1

        return result
    
    # O(n) time and O(1) space
    def reverseInPlace(self, s: List[chr], i: int, j: int) -> None:
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    # O(n ^ 2) time and O(n) space
    def reverseWordsQuadraticTimeAndLinearSpace(self, s: str) -> str:
        # covert string into array (mutable type)
        strAsArray = list(s)
        strAsArray.reverse()

        i = 0
        j = 0
        while i < len(strAsArray):
            if j < len(strAsArray) and strAsArray[j] != ' ':
                j += 1
            else:
                self.reverseInPlace(strAsArray, i, j - 1)
                j += 1
                i = j
        
        while strAsArray[-1] == ' ':
            strAsArray.pop()
        
        while strAsArray[0] == ' ':
            strAsArray.pop(0)
    
        k = 0
        isPrecededWithSpace = False
        while k < len(strAsArray):
            if strAsArray[k] == ' ':
                if isPrecededWithSpace == True:
                    strAsArray.pop(k)
                else:
                    isPrecededWithSpace = True
                    k += 1
            else:
                isPrecededWithSpace = False
                k += 1

        return ''.join(strAsArray)

    def reverseWords(self, s: str) -> str:
        return self.reverseWordsLinearTimeAndLinearSpace(s)