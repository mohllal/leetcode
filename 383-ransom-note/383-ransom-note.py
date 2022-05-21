class Solution:
    # O(n) time and O(n) space
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = {}
        for char in magazine:
            if char not in hashTable:
                hashTable[char] = 1
            else:
                hashTable[char] += 1

        for char in ransomNote:
            if char not in hashTable or hashTable[char] == 0:
                return False
            hashTable[char] -= 1

        return True