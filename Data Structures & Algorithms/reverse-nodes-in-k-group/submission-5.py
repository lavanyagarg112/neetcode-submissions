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

        k_nodes = [head]
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next
            if length % k == 0:
                k_nodes.append(temp)

        if length < k:
            return head

        groups = length // k
        res = None
        curr = head
        prev = None

        for _ in range(groups):
            first_node, next_node = self.reverseList(curr, k)
            if res == None:
                res = first_node
                prev = curr
                curr = next_node
            else:
                prev.next = first_node
                prev = curr
                curr = next_node
        
        prev.next = curr

        return res


        