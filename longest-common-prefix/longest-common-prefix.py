class Solution:
    # O(n * s) time and O(n) space
    def longestCommonPrefixQuadraticTimeAndLinearSpace(self, strs: List[str]) -> str:
        hashTable = {}
        for element in strs:
            for i in range(0, len(element)):
                substr = element[:i + 1]
                if substr in hashTable:
                    hashTable[substr] += 1
                else:
                    hashTable[substr] = 1

        maximum = -1
        result = ''
        for element in hashTable:
            if hashTable[element] >= maximum and len(element) > len(result):
                result = element
                maximum = hashTable[element]
        
        return result if (maximum == len(strs)) else ''
    
    # O(n * s) time and O(1) space
    def longestCommonPrefixQuadraticTimeAndConstantSpace(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if len(prefix) == 0:
                    return ''

        return prefix                

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefixQuadraticTimeAndConstantSpace(strs)