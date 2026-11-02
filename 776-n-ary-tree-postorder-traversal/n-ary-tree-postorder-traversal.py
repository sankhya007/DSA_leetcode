"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node): 
            if not node: 
                return 

            # children is the array of childs that the node has
            # we are looping through that and appending that in our array
            # when found child nodes in a node, loop from each of the child nodes one by one
            for child in node.children: 
                dfs(child)
            res.append(node.val)

        dfs(root)
        return res