class Solution:
    # O(n * logn) time and O(n) space
    def sortedSquaresLogLinearTimeAndLinearSpace(self, nums: List[int]) -> List[int]:
        squares = [num ** 2 for num in nums]
        return sorted(squares)
    
    # O(n) time and O(n) space
    def sortedSquaresLinearTimeAndLinearSpace(self, nums: List[int]) -> List[int]:
        squares = []
        
        minimum_element = abs(nums[0])
        minimum_element_index = 0
        for i in range(len(nums)):
            if abs(nums[i]) < minimum_element:
                minimum_element = abs(nums[i])
                minimum_element_index = i

        left = minimum_element_index
        right = minimum_element_index + 1
        
        while left >= 0 and right <= len(nums) - 1:
            if abs(nums[left]) <= abs(nums[right]):
                squares.append(nums[left] ** 2)
                left -= 1
            else:
                squares.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            squares.append(nums[left] ** 2)
            left -= 1
        
        while right <= len(nums) - 1:
            squares.append(nums[right] ** 2)
            right += 1
        
        return squares

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return self.sortedSquaresLinearTimeAndLinearSpace(nums)