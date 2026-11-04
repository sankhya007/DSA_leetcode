# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        # we only judge the left because if the left exist we are going to assume that the right will also exist because that is just how the tree is supposed to be given the formulation of the tree that we have in the question itself, and if root.val == 1 return True, else 0, so return False
        if not root.left: 
            return root.val == 1

        if root.val == 2: 
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        
        if root.val == 3: 
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)