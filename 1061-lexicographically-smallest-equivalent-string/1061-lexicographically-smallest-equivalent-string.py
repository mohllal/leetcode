class Solution:
    # O(n) time and O(1) space - where n being the number of english letters
    def union(self, parent, x, y):  
        xParent = self.find(parent, x)
        yParent = self.find(parent, y)
        
        xParentValue = xParent - 97
        yParentValue = yParent - 97
        
        _min = min(xParentValue, yParentValue)
        _max = max(xParentValue, yParentValue)
        parent[_max] = _min
        
    
    # O(n) time and O(1) space - where n being the number of english letters
    def find(self, parent, x):
        xValue = ord(x) - 97
        
        if parent[xValue] == xValue:
            return xValue + 97
        else:
            return self.find(parent, chr(parent[xValue] + 97))

    # O((m * n) + (g * n)) time and O(n + g) space
    # where m being s1/s2 length, g being baseStr length, and n being the number of english letters
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        for i in range(len(s1)):
            self.union(parent, s1[i], s2[i])

        result = ''
        for i in range(len(baseStr)):
            current = self.find(parent, baseStr[i])
            result += chr(current)
        
        return result
            