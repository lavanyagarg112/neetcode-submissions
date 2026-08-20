# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # iteration

        # if not list1:
        #     return list2

        # if not list2:
        #     return list1

        result = ListNode()
        orig = result # point to the same place

        while list1 and list2:
            if list1.val < list2.val:
                # only need this if result/orig = None
                # if not result:
                #     orig = list1
                #     result = list1
                # else:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        
        if list1:
            result.next = list1
        else:
        # if list2:
            result.next = list2

        return orig.next

        