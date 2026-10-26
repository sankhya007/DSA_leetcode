class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0 

        for i, x in enumerate(nums): 
            # left = the addition of the left side till now
            # total is total, x is the value itself that we are standing on
            if left == total - left - x: 
                return i 
            left += x

        return -1
