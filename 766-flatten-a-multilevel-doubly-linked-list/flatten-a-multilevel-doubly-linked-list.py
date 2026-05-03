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
            return head 
        
        def dfs(node): 
            current = node
            last = node

            while current: 
                nxt = current.next

                if current.child: 
                    child_last = dfs(current.child)
                    
                    current.next = current.child
                    current.child.prev = current

                    if nxt: 
                        child_last.next = nxt 
                        nxt.prev = child_last

                    current.child = None
                    last = child_last 

                else: 
                    last = current

                current = nxt 
            
            return last 
        
        dfs(head)
        return head