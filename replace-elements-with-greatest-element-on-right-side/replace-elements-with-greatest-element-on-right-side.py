class Solution:
    # O(n ^ 2) time and O(1) space
    def replaceElementsQuadraticTimeAndConstantSpace(self, arr: List[int]) -> List[int]:
        maximum = None
        maximumIndex = None
        for i in range(0, len(arr)):
            if maximum is not None and maximumIndex > i:
                arr[i] = maximum
            else:
                maximum = None
                maximumIndex = None
                for j in range(i + 1, len(arr)):
                    if maximum is None or arr[j] > maximum:
                        maximum = arr[j]
                        maximumIndex = j
                arr[i] = maximum

        arr[-1] = -1
        return arr

    # O(n) time and O(1) space
    def replaceElementsLinearTimeAndConstantSpace(self, arr: List[int]) -> List[int]:
        maximum = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            tmp = maximum
            if arr[i] > maximum:
                maximum = arr[i]
            arr[i] = tmp

        arr[-1] = -1
        return arr

    def replaceElements(self, arr: List[int]) -> List[int]:
        return self.replaceElementsLinearTimeAndConstantSpace(arr)