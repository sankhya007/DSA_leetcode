class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        periodic_sum = 0
        for i in range(len(nums)):
            periodic_sum += nums[i] 
            ans[i] = periodic_sum
        return ans