class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums: 
            if count == 0: 
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate
nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))