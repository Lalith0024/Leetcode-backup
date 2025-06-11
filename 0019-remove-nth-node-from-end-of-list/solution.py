# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = 0
        while curr:
            c += 1
            curr = curr.next
        
        to_be_removed = c - n
        
        # Special case: remove head
        if to_be_removed == 0:
            return head.next
        
        curr = head
        temp = 0
        while curr:
            if temp == to_be_removed - 1:
                curr.next = curr.next.next
                break
            temp += 1
            curr = curr.next
        
        return head

