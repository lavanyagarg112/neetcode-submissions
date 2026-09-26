# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head, length):
        # by design, length should never be more than actual nodes
        curr = head
        prev = head

        for _ in range(length):
            if curr == prev:
                curr = curr.next
                continue
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev, curr
            

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # O(1) space
        # O(n) time

        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        if length < k:
            return head

        groups = length // k
        res = None
        curr = head
        prev = None

        for _ in range(groups):
            first_node, next_node = self.reverseList(curr, k)
            if res == None:
                res = first_node # the start of the new reverse
                prev = curr # the start of the initial, which is end of the reverse list
                curr = next_node # the next group 
            else:
                prev.next = first_node
                prev = curr
                curr = next_node
        
        prev.next = curr # the end node after n/k groups points to the next group (None or node)

        return res


        