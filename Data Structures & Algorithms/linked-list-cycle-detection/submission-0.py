# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # can have a visited set - space: O(n)

        # without visited set - slow and fast pointer

        slow = head
        fast = head.next

        while slow and fast:
            if slow == fast:
                return True 
            
            slow = slow.next

            if not fast.next:
                return False

            fast = fast.next.next

        return False
        