# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy 
        carry = 0

        while l1 or l2 or carry: 
            # this is here we are initiating the values if there is a value in l1 then take that value and of there is none then take it as 0 and it is same for the v2
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # get the numbers 
            total = v1 + v2 + carry # the total of the element v1 v2 and carry,for the 1st val the carry would be 0 
            carry = total // 10 # the 1st element '3'4
            val = total % 10 # the 2nd element 3'4'

            current.next = ListNode(val) # creating a new node and adding the val to that because we are creating a ew lined list when adding the vals
            current = current.next # point to the next 

            # go to the next val in the lists that we have and keep on adding till no values left
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 

        return dummy.next