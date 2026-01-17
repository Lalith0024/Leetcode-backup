# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = ListNode(None)
        prev.next = head
        dummy = prev  # keep reference to dummy head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr  # move prev ONLY if not deleting
            curr = curr.next

        return dummy.next

