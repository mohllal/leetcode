class Solution:
    # O(n ^ 2) time and O(n) space
    def longestCommonPrefix(self, strs: List[str]) -> str:
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