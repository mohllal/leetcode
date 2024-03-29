class Solution:
    def dfs(self, node, parent, adjacent, hasApple):
        if node not in adjacent:
            return 0

        totalTime = 0
        for child in adjacent[node]:
            if child == parent:
                continue
           
            childTime = self.dfs(child, node, adjacent, hasApple)
            if childTime > 0 or hasApple[child]:
                totalTime += 2 + childTime
        
        return totalTime

    # O(n) time and O(n) space
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacent: DefaultDict[int, []]= defaultdict(lambda: [])
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])

        return self.dfs(0, -1, adjacent, hasApple)
