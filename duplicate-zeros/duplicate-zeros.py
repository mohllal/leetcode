class Solution:
    # O(n) time and O(1) space
    def shift(self, arr: List[int], index: int) -> None:
        start = len(arr) - 2
        end = index - 1
        for i in range(start, end, -1):
            arr[i + 1] = arr[i]
    
    # O(n ^ 2) time and O(1) space
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        n = len(arr)
        while i < len(arr):
            if arr[i] == 0:
                self.shift(arr, i)
                i += 2
            else:
                i += 1