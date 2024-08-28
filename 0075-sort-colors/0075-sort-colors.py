class Solution:
    # O(n) time and O(1) space
    def sortColors(self, nums: List[int]) -> None:
        last_red = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[last_red], nums[i] = nums[i], nums[last_red]
                last_red += 1
                
        last_blue = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[last_blue], nums[i] = nums[i], nums[last_blue]
                last_blue -= 1
     
        return nums