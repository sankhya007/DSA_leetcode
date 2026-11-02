# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        # this is the recursive BFS, DFS way
        # if not root: 
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iterative DFS way, stack
        # in the 1st element we srite root to make sure that in the start of the loop the function calls the whole tree
        stack = [[root, 1]]
        res = 0 

        while stack: 
            # pop an element
            node, depth = stack.pop()

            # if the node exists, call the left and the right child element, and keep on increasing the depth by one on each iteration
            # keep on collecting the max depth from each iteration
            if node: 
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res
