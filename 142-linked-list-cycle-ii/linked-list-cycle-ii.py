# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast: 
                break # if we find a cycle in here then we are going to break the cycle because we know that there is a cycle in the linked list 
            
        if not fast or not fast.next: #  this is if something gets in the identifying and if something is wrong with the fast pointer meaning this will return none if those values are empty 
            return None

        slow = head # making slow point towards the head or the start of the list

        # here we are waiting till both of the values are same 
        # because we are posting the value of the slow pointer to the startr of the linked list and then we are incrementing both of them by one in each step they are going to meet at some point because the fast pointer is also the same distance away from the target or the start of the loop, because it is inside the loop, and where both of the pointers meets that value is going to be the starting value of the loop 
        while slow != fast: 
            slow = slow.next
            fast = fast.next

        return fast # anything (fast or slow) will work here because both of them are pointing towards the same element
        
