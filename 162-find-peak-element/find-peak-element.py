class Solution(object):
    def findPeakElement(self, nums):
        peek = max(nums)

        for i, num in enumerate(nums): 
            if num == peek: 
                return i

                