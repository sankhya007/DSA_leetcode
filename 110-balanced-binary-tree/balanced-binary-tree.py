# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root): 
            if not root: 
                return [True, 0]
                # because if there is no attached element with the root there will be no depth and ans will be true

            # no need to calculate depth here in this step
            left = dfs(root.left)
            right = dfs(root.right)

            # while left[0] and right[0] means they have to be true, mening that the pointer have to be in the last element, and the difference of them has to be ether 1 or lesser than 1
            # balanced is a boolean 
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # we are letting the one be there because that is what we mean by balanced
            
            # so in the return we are going to return the depth
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]