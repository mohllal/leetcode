class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) time and O(n) space
    def isPalindromeLinearTimeAndLinearSpace1(self, head: Optional[ListNode]) -> bool:
        nodes = []
        
        temp = head
        while temp is not None:
            nodes.append(temp.val)
            temp = temp.next
        
        n = len(nodes)        
        for i in range(n // 2):
            if nodes[i] != nodes[n - 1 - i]:
                return False
        
        return True
    
    # O(n) time and O(n) space
    def isPalindromeLinearTimeAndLinearSpace2(self, head: Optional[ListNode]) -> bool:
        currentNode = head
    
        def isPalindromeHelper(node):
            nonlocal currentNode
        
            if node is None:
                return True
            
            if not isPalindromeHelper(node.next):
                return False

            isPalindrome = currentNode.val == node.val
            currentNode = currentNode.next

            return isPalindrome

        return isPalindromeHelper(head)
    
    # O(n) time and O(1) space
    def isPalindromeLinearTimeAndConstantSpace(self, head: Optional[ListNode]) -> bool:
        # O(n) time and O(1) space
        def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
            prev_node = None
            current = node
            
            while current is not None:
                next_node = current.next
    
                current.next = prev_node
                prev_node = current

                current = next_node
                
            return prev_node

        # O(n) time and O(1) space
        def getMiddleNode(node: Optional[ListNode]) -> Optional[ListNode]:
            slow = node
            fast = node
            
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
            return slow

        second_half = getMiddleNode(head)
        reversed_second_half = reverseList(second_half)
        
        pointer1 = head
        pointer2 = reversed_second_half
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val != pointer2.val:
                break
    
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        reverseList(reversed_second_half)
        return True if pointer2 is None else False
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.isPalindromeLinearTimeAndConstantSpace(head)
