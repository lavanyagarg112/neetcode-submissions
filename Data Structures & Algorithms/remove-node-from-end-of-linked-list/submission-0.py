# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def listLength(self, head: Optional[ListNode]) -> int:
        length = 0

        while head:
            length += 1
            head = head.next

        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        length = self.listLength(head)
        nthStart = length - n

        if nthStart == 0:
            return head.next

        ans = head

        while nthStart != 1: # while the next one is not the one we want to remove
            ans = ans.next
            nthStart -= 1
        
        if ans.next:
            ans.next = ans.next.next

        return head





