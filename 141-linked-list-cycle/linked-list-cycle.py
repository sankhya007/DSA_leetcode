# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast: # if at any point of the code the slow and the fast pointer is the same that means it has a loop in the linked lsit
                return True
            
        return False 

    # 1 → 2 → 3 → 4 → 5
    #         ↑       ↓
    #          ← ← ← ←
    # when fast reaches 5 the slow is at 3 
    # now because of the loop the fast is going to move to 4 ( 5 - 3 - 4 # double skip)
    # and the slow is going to move to 4 ( 3 - 4 # single skip)
    # both are at the same node, means there is a loop in the linked list
