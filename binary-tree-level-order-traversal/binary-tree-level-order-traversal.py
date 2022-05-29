class TreeNode:
    def __init__(self, val=0, left=None, right=None, level=None):
        self.val = val
        self.left = left
        self.right = right
        self.level = level

class Solution:
    # O(n) time and O(n) space
    def levelOrderIterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        root.level = 0
        levelorder = []
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)

            if len(levelorder) < node.level + 1:
                levelorder.append([node.val])
            else:
                levelorder[-1].append(node.val)
    
            if node.left:
                node.left.level = node.level + 1
                queue.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                queue.append(node.right)
    
        return levelorder
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrderIterative(root)
        