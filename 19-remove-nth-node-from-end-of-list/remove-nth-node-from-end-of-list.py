# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # creating a node, val = 0 and the pointer is head 
        slow = dummy 
        fast = dummy # the slow andd the fast pointers are meant to point to the head but we created a dummy node which is not the head so they are pointing to the dummy 

        for _ in range(n): # n is the index of the element we want to remove ,so we forward fast pointer by n steps
            fast = fast.next
        
        while fast.next: # now we increment both by one step till there is no element left in the list
            slow = slow.next 
            fast = fast.next

        slow.next = slow.next.next # skipping the element that we want to delete 

        return dummy.next # skipping the head when we are printing the array, coz it was dummy 

