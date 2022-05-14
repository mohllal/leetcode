class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = 1 + self.maxDepthRecursive(root.left)
        right = 1 + self.maxDepthRecursive(root.right)

        return max(left, right)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthRecursive(root)
        