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

        return prev
            

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # naive
        # step 1: identify the k+1 starting nodes
        # step 2: reverse them

        k_nodes = [head]
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next
            if length % k == 0:
                k_nodes.append(temp)

        # for node in k_nodes:
        #     if node:
        #         print(node.val)
        #     else:
        #         print("None")

        if length < k:
            return head

        groups = length // k
        res = None

        for i in range(groups):
            first_node = self.reverseList(k_nodes[i], k)
            if i == 0:
                res = first_node
            else:
                k_nodes[i-1].next = first_node

        k_nodes[-2].next = k_nodes[-1]

        return res


        