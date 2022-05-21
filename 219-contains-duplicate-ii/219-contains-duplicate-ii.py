class Solution:
    # O(n * log n) time and O(1) space
    def containsNearbyDuplicateLinearithmicTimeAndConstantSpace(self, nums: List[int], k: int) -> bool:
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
    
    # O(n) time and O(n) space
    def containsNearbyDuplicateLinearTimeAndLinearSpace1(self, nums: List[int], k: int) -> bool:
        hashTable = {}
        
        for i in range(0, len(nums)):
            if nums[i] in hashTable:
                indexes = hashTable[nums[i]]
                for index in indexes:
                    if abs(i - index) <= k:
                        return True
                hashTable[nums[i]].append(i)
            else:
                hashTable[nums[i]] = [i]

        return False

    # O(n) time and O(n) space
    def containsNearbyDuplicateLinearTimeAndLinearSpace2(self, nums: List[int], k: int) -> bool:
        hashTable = {}

        for i in range(0, len(nums)):
            if nums[i] in hashTable:
                diff = abs(hashTable[nums[i]] - i)
                if diff <= k:
                    return True
            hashTable[nums[i]] = i

        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return self.containsNearbyDuplicateLinearTimeAndLinearSpace2(nums, k)