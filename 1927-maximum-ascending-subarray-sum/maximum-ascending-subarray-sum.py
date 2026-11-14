class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)): 
            if nums[i-1] < nums[i]: 
                current += nums[i]
            else: 
                current = nums[i] 

            best = max(best, current)

        return best