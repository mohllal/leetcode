class Solution:
    def containsNearbyDuplicateSlower(self, nums: List[int], k: int) -> bool:
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

    def containsNearbyDuplicateSlower2(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            nums[i] = (nums[i], i)
        
        nums.sort(key=lambda num:num[0])
        
        val, index = nums[0]
        for i in range(1, len(nums)):
            current, j = nums[i]
            if current == val and abs(index - j) <= k:
                return True
            val, index = nums[i]

        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = {}

        for i in range(0, len(nums)):
            if nums[i] in hashtable:
                diff = abs(hashtable[nums[i]] - i)
                if diff <= k:
                    return True
            hashtable[nums[i]] = i

        return False