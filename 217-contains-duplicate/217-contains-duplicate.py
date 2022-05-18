class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        
        for i in range(0, len(nums)):
            if nums[i] in hashtable:
                return True
            else:
                hashtable[nums[i]] = True

        return False