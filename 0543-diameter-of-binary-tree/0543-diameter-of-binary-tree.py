class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(h) space
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = float("-inf")

        def diameterOfBinaryTreeHelper(tree):
            nonlocal diameter

            if tree is None:
                return 0

            left = diameterOfBinaryTreeHelper(tree.left)
            right = diameterOfBinaryTreeHelper(tree.right)

            diameter = max(left + right, diameter)

            return 1 + max(left, right)
        
        diameterOfBinaryTreeHelper(root)
        return diameter
        