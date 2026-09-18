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
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next

            if slow == fast: 
                return True

        return False