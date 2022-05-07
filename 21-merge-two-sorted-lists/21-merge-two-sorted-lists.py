class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def clone(head, node, tail):
    if head is None:
        head = ListNode(node.val, None)
        tail = head
    else:
        tail.next = ListNode()
        tail = tail.next
        tail.val = node.val
        tail.next = None
    return head, tail

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        tail = None
        
        while list1 is not None:
            if list2 is None or list1.val < list2.val:
                result, tail = clone(result, list1, tail)
                list1 = list1.next
            else:
                result, tail = clone(result, list2, tail)
                list2 = list2.next

        while list2 is not None:
            result, tail = clone(result, list2, tail)
            list2 = list2.next
        
        return result  
        
            
            
            
            