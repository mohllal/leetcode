class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(1) time and O(1) space
    def clone(self, head, node, tail):
        if head is None:
            head = ListNode(node.val, None)
            tail = head
        else:
            tail.next = ListNode()
            tail = tail.next
            tail.val = node.val
            tail.next = None
        return head, tail

    # O(n) time and O(1) space
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        tail = None
        
        while list1 is not None:
            if list2 is None or list1.val < list2.val:
                result, tail = self.clone(result, list1, tail)
                list1 = list1.next
            else:
                result, tail = self.clone(result, list2, tail)
                list2 = list2.next

        while list2 is not None:
            result, tail = self.clone(result, list2, tail)
            list2 = list2.next
        
        return result