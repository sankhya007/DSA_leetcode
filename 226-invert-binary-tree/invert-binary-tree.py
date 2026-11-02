# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # if not root: 
        #     return None
        
        # # for every prent node we are going to swap the left and right child nodes, lol
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        if not root: 
            return None 
        
        queue = deque([root]) 
        # this [root] is to make sure that we have the 1st node itself in the queue itself, and then we do the swaps
        while queue: 
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        return root