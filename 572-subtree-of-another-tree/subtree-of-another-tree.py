# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        # if subroot contains nothing ofc that would be true, else False
        if not subRoot: 
            return True
        if not root: 
            return False

        # if the subtree is the complete same as the root means true, ofc
        if self.sameTree(root, subRoot): 
            return True
        # because the subtree has to be a part of the root, check if the left or the right is showed as root if that compared to subroot would that be True or nah
        # call isSubtree and not sametree because if not same we can call same tree again and again, there is not gurantee that this will work on the 1st try
        return ((self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)))

    def sameTree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # means no elements left, return true
        if not root and not subRoot: 
            return True
        # if contains elements and value same, recurse
        if root and subRoot and root.val == subRoot.val: 
            # we go deep in left and deep in right, just like in the last question we were doing, we were saving the left and the right elements together so then this exact thing can happen later on
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False


# root = [3,4,5,1,2]
# subRoot = [4,1,2]

# sol = Solution()
# print(sol.isSubtree(root, subRoot))