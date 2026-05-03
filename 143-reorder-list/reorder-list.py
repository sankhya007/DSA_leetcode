# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: 
            return 

        slow = head
        fast = head.next # here we want the slow pointer to stay at the previous index of the mid thats why we have forwarded the fast by one element 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next # find the mid position

        second = slow.next
        prev = slow.next = None # here we are partitioning the list into two 
        # 1st part the header is head and for the 2nd part the header is None or prev
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp # reverse the 2nd part 

        # now merge the 2nd part
        first = head 
        second = prev # head pointers for both of the lists 
        while second: 
            temp1, temp2 = first.next, second.next # pointers 
            first.next = second # 2nd element 
            second.next = temp1 # 3rd element
            first, second = temp1, temp2 # increment 


        