# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def printList(self, head: Optional[ListNode], string: Optional[str]) -> None:
        if string:
            print("new list", string)
        else:
            print("new list")
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next
        print("end of list")


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        rev_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev_list

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Get median of the list
        orig = head
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        revnext = self.reverseList(slow.next) # get reverse of next
        slow.next = None
            
        restart = orig

        # self.printList(orig, "orig")
        # self.printList(revnext, "revnext")

        while revnext:
            restart_next = restart.next
            revnext_next = revnext.next
            restart.next = revnext
            restart.next.next = restart_next
            restart = restart_next
            revnext = revnext_next
            # self.printList(head, "head")
            # self.printList(restart, "restart")
            # self.printList(revnext, "revnext")

        return

        








