class Solution:
    def findDuplicates(self, nums):
        num_set = set() # storing them in a set
        duplicates = set() # making sure the duplicates list does not have any duplicates
        for num in nums: 
            if num in num_set: 
                duplicates.add(num)
            else: # num not in num_set
                num_set.add(num)
        return list(duplicates) # turning them into a list from a set

nums = [4,3,2,7,8,2,3,1]
solution = Solution()
print(solution.findDuplicates(nums))