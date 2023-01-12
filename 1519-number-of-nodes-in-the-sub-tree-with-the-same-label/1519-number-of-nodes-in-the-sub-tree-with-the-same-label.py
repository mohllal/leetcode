class Solution:
    # O(m) time and O(1) space - m being the number of English letters thus O(1)
    def mergeDicts(self, source, target):
        for key, val in source.items():
                if key in target:
                    target[key] += val
                else:
                    target[key] = val
        return target

    # O(n) time and O(m) space - m being the number of English letters thus O(1)
    def dfs(self, node, parent, adjacent, labels, result):
        if node not in adjacent:
            return
        
        counter = defaultdict(lambda: 0)
        for child in adjacent[node]:
            if child == parent:
                continue
           
            childCounter = self.dfs(child, node, adjacent, labels, result)
        
            counter[labels[child]] += 1    
            counter = self.mergeDicts(childCounter, counter)
    
            result[node] = counter[labels[node]] + 1

        return counter

    # O(n) time and O(n) space
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacent: DefaultDict[int, []]= defaultdict(lambda: [])
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])
        
        result = [1] * n

        self.dfs(0, -1, adjacent, labels, result)
        return result
