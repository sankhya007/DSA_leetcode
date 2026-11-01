# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        prev = dummy
        # dummy is the 1st element of a new array, and prev is the pointer of the head of that nw array

        current = head

        while current: 
            if current.val == val: 
                prev.next = current.next # add that value to the new array 

            else: 
                prev = current

            current = current.next

        return dummy.next