# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head # point tto he 1st element 
        while current and current.next: # if both of them has values in them 
            if current.val == current.next.val: # if the pointer val and the val next to that is same
                current.next = current.next.next # skip the value , print the next 
            else: # if the values are not same, meaning they are not duplicates of each other 
                current = current.next # let it flow normally 
        return head 

    
