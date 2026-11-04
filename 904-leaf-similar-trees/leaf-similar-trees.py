# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(root, leaf): 
            # if the root itself does not have a value return
            if not root: 
                return 
            # if the root neighter have a left or a right child node, meaning it is the leaf itself, append that vale
            if not root.left and not root.right: 
                leaf.append(root.val)
                return 
            # recurse on the left and right
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        # create an empty stack/array for the leaf
        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        
        return leaf1 == leaf2