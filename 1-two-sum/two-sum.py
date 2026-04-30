class Solution:
    def twoSum(self, nums, target): 
        num_set = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_set: 
                return [num_set[complement], i]
            num_set[num] = i

nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))