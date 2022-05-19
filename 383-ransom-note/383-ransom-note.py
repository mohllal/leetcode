class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineHashTable = {}
        for char in magazine:
            if char not in magazineHashTable:
                magazineHashTable[char] = 1
            else:
                magazineHashTable[char] += 1

        for char in ransomNote:
            if char not in magazineHashTable or magazineHashTable[char] == 0:
                return False
            magazineHashTable[char] -= 1

        return True