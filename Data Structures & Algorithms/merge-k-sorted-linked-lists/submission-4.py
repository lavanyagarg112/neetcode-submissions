# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # using heap
        # have to create a way to order the nodes too
        min_heap = []

        curr = result = ListNode(0)

        for lst in lists:
            if lst:
                heappush(min_heap, Node(lst))

        while min_heap:
            smallest = heappop(min_heap).node
            curr.next = smallest
            curr = curr.next
            if smallest.next:
                heappush(min_heap, Node(smallest.next))
        
        return result.next






        


        