# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # time: O(max (m,n))
        carry = 0
        result = curr = None

        p1 = l1
        p2 = l2

        while p1 or p2:
            res = carry
            if p1:
                res += p1.val
                p1 = p1.next
            if p2:
                res += p2.val
                p2 = p2.next
            carry = res // 10
            res = res % 10
            if curr == None:
                result = curr = ListNode(res)
            else:
                curr.next = ListNode(res)
                curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return result
