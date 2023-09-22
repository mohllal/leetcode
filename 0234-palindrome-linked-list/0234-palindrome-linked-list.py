class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.isPalindromeRecursiveLinearTimeAndLinearSpace(head)
    
    # O(n) time and O(n) space
    def isPalindromeRecursiveLinearTimeAndLinearSpace(self, head):
        headNode = head
    
        def isPalindromeHelper(node):
            nonlocal headNode
        
            if node is None:
                return True
            
            if not isPalindromeHelper(node.next):
                return False
            
            isPalindrome = node.val == headNode.val
            headNode = headNode.next
            
            return isPalindrome
        
        return isPalindromeHelper(head)
    
    
    # O(n) time and O(n) space
    def isPalindromeIterativeLinearTimeAndLinearSpace(self, head):
        stack = []

        node = head
        while node is not None:
            stack.append(node)
            node = node.next
        
        headNode = head
        while len(stack) != 0:
            node = stack.pop()
            
            if headNode.val != node.val:
                return False
            
            headNode = headNode.next
        
        return True