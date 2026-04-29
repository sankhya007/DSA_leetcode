class Solution:
    def findDuplicates(self, nums):
        num_set = set()
        duplicates = set()
        for num in nums: 
            if num in num_set: 
                duplicates.add(num)
            else: 
                num_set.add(num)
        return list(duplicates)

nums = [4,3,2,7,8,2,3,1]
solution = Solution()
print(solution.findDuplicates(nums))