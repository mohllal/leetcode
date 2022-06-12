class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # O(n + m) time and O(n) space
    def cloneRecursive(self, node: Node, visited) -> Node:
        if not node:
            return

        if node in visited:
            return visited[node]
        
        newNode = Node(node.val)
        visited[node] = newNode
        
        for neighbor in node.neighbors:
            current = self.cloneRecursive(neighbor, visited)
            newNode.neighbors.append(current)

        return newNode 
        
    def cloneGraph(self, node: Node) -> Node:
        return self.cloneRecursive(node, {})