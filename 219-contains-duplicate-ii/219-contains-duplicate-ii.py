class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = {}
        
        for i in range(0, len(nums)):
            if nums[i] in hashtable:
                indexes = hashtable[nums[i]]
                for index in indexes:
                    if abs(i - index) <= k:
                        return True
                hashtable[nums[i]].append(i)
            else:
                hashtable[nums[i]] = [i]

        return False