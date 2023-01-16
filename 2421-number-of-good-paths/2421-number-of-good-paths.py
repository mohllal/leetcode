class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
 
    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] = self.rank[y] + 1

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        adjacent: DefaultDict[int, list] = defaultdict(lambda: [])
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])
            
        valuesToNodes: DefaultDict[int, list] = defaultdict(lambda: [])
        for i in range(n):
            valuesToNodes[vals[i]].append(i)
        
        valuesToNodesSortedItems = sorted(valuesToNodes.items(), key=lambda x: x[0])
        
        disjointSet = DisjointSet(n)
        goodPaths = 0
        for val, nodes in valuesToNodesSortedItems:
            for node in nodes:
                for child in adjacent[node]:
                    if vals[child] <= val:
                        disjointSet.union(child, node)
            
            group: DefaultDict[int, int] = defaultdict(lambda: 0)
            for node in nodes:
                parent = disjointSet.find(node)
                group[parent] += 1
            
            for _, paths in group.items():
                goodPaths += paths * (paths + 1) // 2
        return goodPaths