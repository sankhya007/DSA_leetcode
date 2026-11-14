class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_count = 1 
        decreasing_count = 1 
        best = 1

        for i in range(len(nums)-1): 
            if nums[i] < nums[i+1]: 
                increasing_count += 1
                decreasing_count = 1

            elif nums[i] > nums[i+1]: 
                decreasing_count += 1
                increasing_count = 1

            else: 
                increasing_count = 1
                decreasing_count = 1

            best = max(best, increasing_count, decreasing_count)

        return best