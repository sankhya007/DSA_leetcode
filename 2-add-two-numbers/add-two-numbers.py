# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        # head node is the new dummy node 
        dummy = ListNode(0)

        # we start the count form the current
        current = dummy 
        carry = 0 

        # keep going till one of them has a digit
        while l1 or l2 or carry: 

            # if one of the list is short add zeros in the place of that
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            total = v1 + v2 + carry 

            # 15 // 10 = 1 (carry)
            # 15 % 10 = 5 (val)
            carry = total // 10 
            val = total % 10 

            # this is to create a new node where we are going to store the value that we have gotten
            current.next = ListNode(val)

            # move to the next node in the new storage list 
            current = current.next

            # now we also move to the next node in the lists that we are counting 
            if l1: l1 = l1.next
            if l2: l2 = l2.next 

        # point to the head node
        return dummy.next 
