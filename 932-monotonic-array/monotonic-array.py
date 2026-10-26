class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        
        length = len(nums)
        increasing = True
        decreasing = True

        for i in range(1, length): 
            if nums[i] > nums[i-1]: 
                decreasing = False
            if nums[i] < nums[i-1]:
                increasing = False

        return increasing or decreasing