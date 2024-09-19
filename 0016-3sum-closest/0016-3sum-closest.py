class Solution:
    # O(n * log n) time and O(1) space
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                diff = target - (nums[i] + nums[j] + nums[k])
                
                if abs(diff) < abs(closest):
                    closest = diff
                
                if diff > 0:
                    j += 1
                elif diff < 0:
                    k -= 1
                else:
                    return target - closest

        return target - closest