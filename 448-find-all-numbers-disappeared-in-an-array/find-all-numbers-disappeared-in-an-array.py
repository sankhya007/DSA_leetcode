class Solution:
    def findDisappearedNumbers(self, nums): 
        n = len(nums) 
        num_set = set(nums) # get rid of all the duplicates in the array 
        missing_numbers = [] # storage for missing number/s
        for i in range(1, n+1): 
            if i not in num_set: 
                missing_numbers.append(i)
        return missing_numbers

nums = [4,3,2,7,8,2,3,1]
solution = Solution()
print(solution.findDisappearedNumbers(nums))
