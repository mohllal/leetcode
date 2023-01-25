class Solution:
    def bfs(self, n, adjacency, start):
        distances = [None] * n
        queue = deque([start])
        distances[start] = 0

        while queue:
            current = queue.popleft()
            
            for node in adjacency[current]:
                if distances[node] == None:
                    distances[node] = distances[current] + 1
                    queue.append(node)
        
        return distances
         
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        adjacency: DefaultDict[int, list] = defaultdict(lambda: [])
        for i in range(len(edges)):
            if edges[i] != -1:
                adjacency[i].append(edges[i])
            
        nodeOneDistances = self.bfs(n, adjacency, node1)
        nodeTwoDistances = self.bfs(n, adjacency, node2)

        result = -1
        minimum = float("inf")
        for i in range(n):
            if nodeOneDistances[i] == None or nodeTwoDistances[i] == None:
                continue
            
            if max(nodeOneDistances[i], nodeTwoDistances[i]) < minimum:
                minimum = max(nodeOneDistances[i], nodeTwoDistances[i])
                result = i
            
        return result
        
        
        