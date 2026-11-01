# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 

        # here we are checking till the fast and the slow pointer end up at the same value, if they do meaning the linked list does have a cycle
        # fast is checking if fast itself exists or not because then there will be no fast.next
        # and fast.next is cheking if fast.next exist or not because else there wil be no fast.next.next if any of them are null
        # slow is something that is following the fast meaning the elements for the slow definately exists
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next

            if slow == fast: 
                return True

        return False