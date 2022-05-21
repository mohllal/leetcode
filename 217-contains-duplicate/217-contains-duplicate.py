class Solution:
    # O(n) time and O(n) space
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        
        for i in range(0, len(nums)):
            if nums[i] in hashTable:
                return True
            else:
                hashTable[nums[i]] = True

        return False