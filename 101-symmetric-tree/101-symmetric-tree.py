class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricRecursive(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if (left is None and right is not None) or (right is None and left is not None):
                return False
        
        if (left is not None and right is not None) and left.val != right.val:
                return False

        if left is None and right is None:
                return True

        isFirstHalfSymmetric = self.isSymmetricRecursive(left.left, right.right)
        isSecondHalfSymmetric = self.isSymmetricRecursive(left.right, right.left)
        
        return isFirstHalfSymmetric and isSecondHalfSymmetric
 
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        leftQueue = [root.left]
        rightQueue = [root.right]
        
        while len(leftQueue) > 0 or len(rightQueue) > 0:
            if len(leftQueue) == 0:
                return False

            if len(rightQueue) == 0:
                return False

            leftNode = leftQueue.pop(0)
            rightNode = rightQueue.pop(0)

            if (leftNode is None and rightNode is not None) or (rightNode is None and leftNode is not None):
                return False

            if (leftNode is not None and rightNode is not None) and leftNode.val != rightNode.val:
                return False

            if leftNode is None and rightNode is None:
                continue  

            leftQueue.append(leftNode.left)
            leftQueue.append(leftNode.right)

            rightQueue.append(rightNode.right)
            rightQueue.append(rightNode.left)

        return True
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRecursive(root.left, root.right)
        