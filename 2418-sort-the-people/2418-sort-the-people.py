class Solution:
    # O(n * log n) time and O(n) space
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = []
        for i in range(len(names)):
            data.append((names[i], heights[i]))
        
        data.sort(key=lambda elem: elem[1], reverse=True)
        return [elem[0] for elem in data]
