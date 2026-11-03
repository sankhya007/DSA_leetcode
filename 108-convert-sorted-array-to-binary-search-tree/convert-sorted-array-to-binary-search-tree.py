# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums: 
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid]) # mid becomes the top
    
        # left part
        root.left = self.sortedArrayToBST(nums[:mid])
        # right part
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        '''
        keep on recalling the same function till the damn thing does not runs of eleemnts. 
        for the left part find out the mid/ top element of the left part, and simillerly for the right find the top/mid element of the right part
        '''

        return root