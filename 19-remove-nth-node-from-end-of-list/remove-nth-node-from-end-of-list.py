# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
       # make a dummy node before the head, call it head
        dummy = ListNode(0, head)

        # point both of the pointers to the dummy 
        slow = dummy 
        fast = dummy 

        # for however many number we need of the end let the fast pointer go that many times
        for _ in range(n): 
            fast = fast.next 

        # then run the slow and the fast pointer together
        while fast.next: 
            slow = slow.next
            fast = fast.next
        # after this the slow pointer will be at the intended delete position

        # delete the position
        slow.next = slow.next.next

        # return dummy.next because the code might have caused the head to be deleted, but the dummy.next element will always be there
        return dummy.next





