class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = [p]
        qQueue = [q]
        
        while len(pQueue) > 0 or len(qQueue) > 0:
            if len(pQueue) == 0:
                return False
            
            if len(qQueue) == 0:
                return False
            
            pNode = pQueue.pop(0)
            qNode = qQueue.pop(0)
            
            if (pNode is None and qNode is not None) or (qNode is None and pNode is not None):
                return False

            if (pNode is not None and qNode is not None) and pNode.val != qNode.val:
                return False

            if qNode is None and pNode is None:
                continue  

            pQueue.append(pNode.left)
            pQueue.append(pNode.right)
            
            qQueue.append(qNode.left)
            qQueue.append(qNode.right)
            
        return True