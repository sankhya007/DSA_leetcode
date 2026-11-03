# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # keep in mind to store them as one singular element
        stack = [(p, q)]

        while stack: 
            nodep, nodeq = stack.pop()

            # if they are both null, skip over that because at the end the value is actually same
            if not nodep and not nodeq: 
                continue
            # if one of them is null or the values does not match return false
            if not nodep or not nodeq or nodep.val != nodeq.val: 
                return False
            # if the values do exist and they are actually same then we store them as one element in the stack
            stack.append((nodep.left, nodeq.left))
            stack.append((nodep.right, nodeq.right))

        return True