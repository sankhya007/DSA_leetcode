class Solution(): 
    def pivotIndex(self, nums): 
        left = 0 
        total = sum(nums)

        for i, x in enumerate(nums): 
            if left == total - left - x: 
                return i 
            left += x 

        return -1 