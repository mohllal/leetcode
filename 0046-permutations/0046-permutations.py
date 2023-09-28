class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.premuteAggergateAtRootLevelMemoized(nums)

    # O(n*n!) time and O(n*n!) space
    def premuteAggergateAtLeafLevel(self, nums):
        def permuteHelper(nums, prefix, premutations):
            if len(nums) == 0 and len(prefix) > 0:
                premutations.append(prefix)
                return

            # using array slicing instead of set
            # for i in range(len(nums)):
            #     newNums = nums[:i] + nums[i+1:]
            #     newPrefix = prefix + [nums[i]]
            #     permuteHelper(newNums, newPrefix, premutations)
            
            newNums = set(nums)
            for num in nums:
                newNums.remove(num)
                newPrefix = prefix + [num]
                permuteHelper(newNums, newPrefix, premutations)
                newNums.add(num)

        premutations = []
        prefix = []
        permuteHelper(nums, prefix, premutations)
        return premutations

    # O(n*n!) time and O(n*n!) space
    def premuteAggergateAtRootLevel(self, nums):
        def permuteHelper(nums):
            if len(nums) == 1:
                return [nums]

            # using array slicing instead of set
            # premutations = []
            # for i in range(len(nums)):
            #     newNums = nums[:i] + nums[i+1:]
            #     currentPremutations = permuteHelper(newNums)
            #     for premutation in currentPremutations:
            #         premutations.append([nums[i]] + premutation)
        
            newNums = set(nums)
            premutations = []
            for num in nums:
                newNums.remove(num)
                currentPremutations = permuteHelper(newNums)
                for premutation in currentPremutations:
                    premutations.append([num] + list(premutation))
                newNums.add(num)
            
            return premutations
        
        premutations = permuteHelper(nums)
        return premutations

    # O(n!) time and O(n*n!) space
    def premuteAggergateAtRootLevelMemoized(self, nums):
        def permuteHelper(nums, memo):
            if len(nums) == 1:
                return [nums]
            
            numsHashable = frozenset(nums)

            if numsHashable in memo:
                return memo[numsHashable]
            
            # using array slicing instead of set
            # premutations = []
            # for i in range(len(nums)):
            #     newNums = nums[:i] + nums[i+1:]
            #     currentPremutations = permuteHelper(newNums, memo)
            #     for premutation in currentPremutations:
            #         premutations.append([nums[i]] + premutation)
            
            newNums = set(nums)
            premutations = []
            for num in nums:
                newNums.remove(num)
                currentPremutations = permuteHelper(newNums, memo)
                for premutation in currentPremutations:
                    premutations.append([num] + list(premutation))
                newNums.add(num)
            
            memo[numsHashable] = premutations
            return premutations
        
        memo = {}
        premutations = permuteHelper(nums, memo)
        return premutations