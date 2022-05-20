class Solution:
    # O(n ^ 2) time and O(1) space
    def checkIfExistQuadraticTimeAndConstantSpace(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if arr[i] * 2 == arr[j] or arr[i] == arr[j] * 2:
                    return True
        return False
    
    # O(n) time and O(n) space
    def checkIfExistLinearTimeAndLinearSpace(self, arr: List[int]) -> bool:
        hashTable = {}
        
        for num in arr:
            if num in hashTable:
                return True
            hashTable[num * 2] = True
            if num % 2 == 0:
                hashTable[num // 2] = True
    
        return False

    def checkIfExist(self, arr: List[int]) -> bool:
        return self.checkIfExistLinearTimeAndLinearSpace(arr)