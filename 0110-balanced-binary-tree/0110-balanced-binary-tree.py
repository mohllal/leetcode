class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(h) space
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def heightBalancedBinaryTreeHelper(tree):
            nonlocal balanced

            if tree is None:
                return 0

            left = heightBalancedBinaryTreeHelper(tree.left)
            right = heightBalancedBinaryTreeHelper(tree.right)

            balanced &= abs(left - right) <= 1

            return 1 + max(left, right)

        heightBalancedBinaryTreeHelper(root)
        return balanced
        