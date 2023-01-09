class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(n) space
    def preorderTraversalRecursive(self, root: Optional[TreeNode], preorder: List[int]) -> List[int]:
        if root is None:
            return
        
        preorder.append(root.val)
        
        left = self.preorderTraversalRecursive(root.left, preorder)
        right = self.preorderTraversalRecursive(root.right, preorder)
        return preorder
    
    # O(n) time and O(n) space
    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        preorder = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return preorder

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        self.preorderTraversalRecursive(root, preorder)
        return preorder