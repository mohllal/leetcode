class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.sum = val

class Solution:
    def hasPathSumRecursive(self, root: Optional[TreeNode], targetSum: int, pathSum: int) -> bool:
        if root is None:
            return False
        
        pathSum += root.val

        if not root.left and not root.right and targetSum == pathSum:
            return True
    
        left = self.hasPathSumRecursive(root.left, targetSum, pathSum)
        right = self.hasPathSumRecursive(root.right, targetSum, pathSum)

        return left or right

    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        root.sum = root.val
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left:
                node.left.sum = node.sum + node.left.val
                queue.append(node.left)

            if node.right:
                node.right.sum = node.sum + node.right.val
                queue.append(node.right)
                
            if not node.left and not node.right and node.sum == targetSum:
                return True

        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        return self.hasPathSumRecursive(root, targetSum, 0)