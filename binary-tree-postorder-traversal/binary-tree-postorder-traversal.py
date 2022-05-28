class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversalRecursive(self, root: Optional[TreeNode], postorder: List[int]) -> List[int]:
        if root is None:
            return

        self.postorderTraversalRecursive(root.left, postorder)
        self.postorderTraversalRecursive(root.right, postorder)
        postorder.append(root.val)

        return postorder

    # O(n) time and O(n) space
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        postorder = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            postorder.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        postorder.reverse()
        return postorder
                
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        self.postorderTraversalRecursive(root, postorder)
        return postorder