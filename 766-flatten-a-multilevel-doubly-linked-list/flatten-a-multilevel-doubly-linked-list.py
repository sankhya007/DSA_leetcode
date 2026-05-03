"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head # return the full list 
        
        def dfs(node):
            current = node
            last = node # will deonte to the mentioned node 

            while current: 
                nxt = current.next # store the value of current in the temp folder next

                if current.child: # if there is a child
                    child_last = dfs(current.child) # get the last element of the child list

                    current.next = current.child 
                    current.child.prev = current # connect the start of the child 

                    if nxt: # if there is anything more left in the list after the child node is flattened add that to the end of the child node 
                        child_last.next = nxt
                        nxt.prev = child_last # connecting the start of the left out list to the end of the child array, now the child array is fullly flattened 

                    current.child = None # because the whole thing is flattened so there is no child pointer left so make that end
                    last = child_last # so here we denote the last element of the child as the last element of the array after seeing if there is a next element or no 

                else: # if there is not a child 
                    last = current # the last element is similler with the present element 

                current = nxt # increment 

            return last # the last element of the connected list, so we can reconnect just like how we asked for the child_last by doing dfs 

        dfs(head) # now do the dfs in the whole list
        return head 
