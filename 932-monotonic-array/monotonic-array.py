class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1, len(nums)): 
            if nums[i-1] < nums[i]: 
                decreasing = False

            if nums[i-1] > nums[i]: 
                increasing = False

        return increasing or decreasing