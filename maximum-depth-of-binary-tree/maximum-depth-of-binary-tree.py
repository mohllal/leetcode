class TreeNode:
    def __init__(self, val=0, left=None, right=None, depth=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.maxDepthRecursive(root.left)
        right = self.maxDepthRecursive(root.right)

        return max(left, right) + 1
    
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        root.depth = 1
        queue = [root]
        depth = 1

        while len(queue) > 0:
            node = queue.pop(0)
    
            if node.left:
                node.left.depth = node.depth + 1
                queue.append(node.left)
            if node.right:
                node.right.depth = node.depth + 1
                queue.append(node.right)
    
            depth = max(depth, node.depth)

        return depth   

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthIterative(root)