class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        inc = dec = 1
        # if nothing then return 1
        best = 1 

        # leave out the 1st index for comparison
        for i in range(1, len(nums)): 

            # if previous number smaller then increase inc
            if nums[i] > nums[i - 1]: 
                inc += 1
                dec = 1

            # if previous number big increase dec
            elif nums[i] < nums[i - 1]: 
                dec += 1
                inc = 1 

            else: 
                inc = dec = 1

            best = max(best, inc, dec)

        return best 