class Solution:
    # O(n) time and O(n) space
    def bfs(self, node, adjacent, values):
        goodPaths = 1
        if node not in adjacent:
            return goodPaths

        queue = deque(adjacent[node])
        visited = set([node])
        while queue:
            current = queue.popleft()
            visited.add(current)

            if values[node] < values[current]:
                continue
        
            if values[node] == values[current]:
                goodPaths += 1

            for child in adjacent[current] - visited:
                queue.append(child)
    
        return goodPaths
    
    # O(n ^ 2) time and O(n ^ 2) space
    def numberOfGoodPathsNaive(self, vals: List[int], edges: List[List[int]]) -> int:
        pass
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        n = len(vals)
        p = list(range(n))
        size = defaultdict(Counter)
        for i, v in enumerate(vals):
            size[i][v] = 1

        ans = n
        for v, a in sorted(zip(vals, range(n))):
            for b in g[a]:
                if vals[b] > v:
                    continue
                pa, pb = self.find(p, a), self.find(p, b)
                if pa != pb:
                    ans += size[pa][v] * size[pb][v]
                    p[pa] = pb
                    size[pb][v] += size[pa][v]
        return ans