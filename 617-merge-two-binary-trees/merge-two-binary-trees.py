# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:

        # this is what we are going to do to do the calculation in one position
        # if not root1: 
        #     return root2
        # if not root2: 
        #     return root1

        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1

        # and to create a new tree and get the value in there do this
        if not root1 and not root2: 
            return None 

        v1 = root1.val if root1 else 0 
        v2 = root2.val if root2 else 0 
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root