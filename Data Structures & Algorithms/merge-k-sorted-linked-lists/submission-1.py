# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_val = float('inf')
        min_ind = None
        min_head = None

        for i in range(len(lists)): # O(k) where k = number of lists
            head = lists[i]

            if head and head.val < min_val:
                min_val = head.val
                min_ind = i
                min_head = head

        if min_ind == None:
            return None

        lists[min_ind] = lists[min_ind].next
        min_head.next = self.mergeKLists(lists) # O(n), where n total nodes overall

        return min_head



        