# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head 
        fast = head
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next
        
        current = slow
        prev = None
        while current:
            next_element = current.next 
            current.next = prev 
            prev = current
            current = next_element

        left = head
        right = prev
        while right: 
            if left.val != right.val: 
                return False
            left = left.next
            right = right.next
        return True