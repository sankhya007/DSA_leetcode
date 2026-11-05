# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        array = []

        # while current because we need the current pointer to end up ad null
        while current: 
            array.append(current)
            current = current.next
        # so after this we have appended the full list1 in the new geenrated array
        array[a - 1].next = list2 # here we are not altering the array rather we are just changing the pointer of that oe singular node that we want to change
        # so now the position a is actually cut of and we are pointing from the a - 1 position to list2's head

        # now the current is pointing towards list 2
        current = list2
        # current.next because we want the pointer to stay at the last element
        while current.next: 
            current = current.next

        current.next = array[b + 1] # like previous we are just pointing to the new pointer what we want it to be, given in the question
        return list1 # because of the newt modifiers that we have made in the pointing in the code to their desired lications and not chainging any of the lists, we are just pointing to things