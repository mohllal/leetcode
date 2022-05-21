class Solution:
    # O(n) time and O(n) space
    def firstUniqChar(self, s: str) -> int:
        hashTable = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in hashTable:
                hashTable[s[i]] = (i, 0)
            else:
                hashTable[s[i]] = (i, hashTable[s[i]][1] + 1)
        
        result = -1
        for key in hashTable:
            if hashTable[key][1] == 0:
                if result == -1:
                    result = hashTable[key][0]
                elif result > hashTable[key][0]:
                    result = hashTable[key][0]

        return result