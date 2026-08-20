# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # divide and conquer

        if not lists:
            return None

        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, start, end):
        if start > end:
            return None

        if start == end:
            return lists[start]

        midpoint = start + ((end - start)//2)
        left = self.divide(lists, start, midpoint)
        right = self.divide(lists, midpoint + 1, end)

        return self.conquer(left, right)

    def conquer(self, list1, list2):
        
        result = curr = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return result.next



