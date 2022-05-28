class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(n) space
    def inorderTraversalRecursive(self, root: Optional[TreeNode], inorder: List[int]) -> List[int]:
        if root is None:
            return

        left = self.inorderTraversalRecursive(root.left, inorder)
        inorder.append(root.val)
        right = self.inorderTraversalRecursive(root.right, inorder)
        
        return inorder

    # O(n) time and O(n) space
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        current = root
        inorder = []

        while len(stack) > 0 or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                inorder.append(current.val)
                current = current.right

        return inorder

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        self.inorderTraversalRecursive(root, inorder)
        return inorder