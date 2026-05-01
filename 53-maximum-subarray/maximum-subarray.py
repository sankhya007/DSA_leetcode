class Solution:
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        # setting both of the values to the 1st element of the array 

        for i in range(1, len(nums)): 
            max_current = max(nums[i], max_current + nums[i])
            # find the maxx form the already existing sum and the adition of the next element
            if max_current > max_global: 
                max_global = max_current 
                # overwrite the global element if the current element is bigger than it

        return max_global
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))