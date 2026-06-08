class Solution:
    def majorityElement(self, nums): 
        n = len(nums)//2
        nums.sort()
        return nums[n]