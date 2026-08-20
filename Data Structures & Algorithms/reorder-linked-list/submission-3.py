# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # rec

        def rec(curr, root):

            if not curr:
                return root

            root = rec(curr.next, root)

            if not root:
                return None

            tmp = None

            if root == curr or root.next == curr:
                curr.next = None

            else:
                tmp = root.next
                root.next = curr
                curr.next = tmp

            return tmp

        head = rec(head.next, head)