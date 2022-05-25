class Solution:
    # O(n ^ 2) time and O(1) space
    def rotateQuadraticTimeAndConstantSpace(self, nums: List[int], k: int) -> None:
        n = len(nums)
        i = 0

        while k > 0:
            elem = nums[n - 1]
            for i in range(n - 1, 0, -1):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

            nums[0] = elem
            k -= 1

    # O(n) time and O(n) space
    def rotateLinearTimeAndLinearSpace(self, nums: List[int], k: int) -> None:
        n = len(nums)
        shifts = k % n
        
        arr = []
        for i in range(shifts - 1, -1, -1):
            arr.append(nums[n - 1 - i])
        
        j = 0
        for i in range(n - shifts - 1, -1, -1):
            nums[i], nums[n - 1 - j] = nums[n - 1 - j], nums[i]
            j += 1
        
        for i in range(0, shifts):
            nums[i] = arr[i]

    def rotate(self, nums: List[int], k: int) -> None:
        self.rotateLinearTimeAndLinearSpace(nums, k)