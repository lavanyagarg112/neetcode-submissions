# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass solution

        start = head
        end = head
        end_p = 1 # move the pointer to the nth node
        
        while end_p != n:
            end = end.next
            end_p += 1

        while end.next and end.next.next: # since have to skip
            start = start.next
            end = end.next

        if start == end:
            return head.next

        start.next = start.next.next
        return head

        

