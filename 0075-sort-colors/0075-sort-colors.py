class Solution:
    # O(n) time and O(1) space
    def sortColorsLinearTimeAndConstantSpace1(self, nums: List[int]) -> None:
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
    
    # O(n) time and O(1) space
    def sortColorsLinearTimeAndConstantSpace2(self, nums: List[int]) -> None:
        red = 0
        blue = len(nums) - 1
        
        current = 0
        while current <= blue:
            if nums[current] == 0:
                nums[current], nums[red] = nums[red], nums[current]
                current += 1
                red += 1
            elif nums[current] == 2:
                nums[current], nums[blue] = nums[blue], nums[current]
                blue -= 1
            else:
                current += 1
                
        return nums

    def sortColors(self, nums: List[int]) -> None:
        return self.sortColorsLinearTimeAndConstantSpace2(nums)