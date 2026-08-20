# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # recursion

        def rec(curr, pos):
            if not curr:
                return pos

            pos = rec(curr.next, pos)
            
            if pos == None:
                return None

            if pos == n:
                if curr.next:
                    curr.next = curr.next.next
                return None
            else:
                return pos + 1

        curr_pos = rec(head, 0)

        if curr_pos == None:
            return head
        else:
            return head.next


        