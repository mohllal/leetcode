from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = deque()
        current = root
        inorder = []

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                inorder.append(current.val)
                current = current.right

        return inorder