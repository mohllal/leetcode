class Solution:
    # O(n) time and O(1) space
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 1
        increasing = True
        
        while i < len(arr):
            if arr[i] == arr[i - 1]:
                return False
            if increasing and arr[i] < arr[i - 1] and i == 1:
                return False
            if increasing and arr[i] > arr[i - 1] and i == len(arr) - 1:
                return False
            if not increasing and arr[i] > arr[i - 1]:
                return False            
            if increasing and arr[i] < arr[i - 1]:
                increasing = False
            i += 1

        return True