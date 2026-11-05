# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        current = head # pointer
        tail = dummy = ListNode() 
        # here up above we have two pointers attached with each other because we need one pointer to call teh node itself that are going to create and the other one is actally going to go forward one by one and then is goign to place the values that we calculate
        while current.next: 
            # create an empty node with the value of zero in it
            node = ListNode(0)
            while current.next.val != 0: 
                node.val += current.next.val
                current = current.next # move the current pointer forward in every step till the statement is true

            tail.next = node # append that value that we just have calculated next to the dummy variable
            tail = tail.next # move the tail to the next position, so then we can put value to the next position
            current = current.next # this line is here only for the time we are going to hit the 0 value in the loop, when the value is 0 we are going to skip that because we do not need to have that value i the result array and or else vecause we are just searching for non zero values we would just not be able to continue the loop if we do not skip it

        return dummy.next