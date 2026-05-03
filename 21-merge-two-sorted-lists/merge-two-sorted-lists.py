# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy 

        while list1 and list2: # loop will run when both th elist has some values in it and none of them are empty
            if list1.val <= list2.val: 
                current.next = list1 # next val chanes to the list1 val
                list1 = list1.next 
            else: 
                current.next = list2 # next val changes to the list2 val
                list2 = list2.next # and the pointer inside the list also increments to the next val

            current = current.next # simillerly the pointer in the current or the area thet we are going to fill the next is also going to shift by one position
            
        if list1: 
            current.next = list1 # if there is any vals left in the list one, we just add them in the last 
        else: 
            current.next = list2 # same for the list2, aif any left add them in the last

        return dummy.next # we added a fake node while adding the dummy and then we pointed to the main linked list and tahts why we are returning dummy.next so then it skps the fake node and prots from the 2nd node, which we have in the list