class Solution:
    def containsDuplicate(self, nums): 
        num_set = set() #making sure that it does not have any duplicates 
        for num in nums: 
            if num in num_set: 
                return True
            else: #meaning the num is not in num_set
                num_set.add(num)
        return False

nums = [1,1,1,3,3,4,3,2,4,2]
solution = Solution()
print(solution.containsDuplicate(nums))