class Solution:
    def missingNumber(self, nums): 
        n = len(nums) + 1 
        expected_sum = n * (n - 1) // 2 
        # this is where we get the actual sum this is the formula 
        # "//" is done to get integer value and if we did "/" then return woould have been a float number
        actual_sum = sum(nums)
        return expected_sum - actual_sum

nums = [9,6,4,2,3,5,7,0,1]
solution = Solution()
print(solution.missingNumber(nums))