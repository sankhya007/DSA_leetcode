class Solution:
    def reverseList(self, head):
        prev = None
        current = head 

        while current: 
            next_node = current.next # store the next node 
            current.next = prev # point the next node to the current 
            prev = current # point the current as previous 
            current = next_node # now the next_node becomes the current node

        return prev
    