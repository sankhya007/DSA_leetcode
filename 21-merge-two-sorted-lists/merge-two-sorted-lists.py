# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        # till there are elemnts in both list 1 and 2
        while list1 and list2: 
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1: 
            current.next = list1
        else:
            current.next = list2

        # return dummy.next because dummy is actually 0, and actually does not exist and artificially created by us
        return dummy.next

