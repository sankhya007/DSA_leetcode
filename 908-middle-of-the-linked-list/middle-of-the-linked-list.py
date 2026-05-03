
class Solution:
    def middleNode(self, head):
        slow = head # slow pointer
        fast = head # fast poinetr 

        while fast and fast.next: # make sure both fast and fast.next has a value 
            slow = slow.next
            fast = fast.next.next # this moves twice as fast so when it is at the end the slow one has gone only half the stsps meaning it is at the middle of the linked list 
        
        return slow 


        