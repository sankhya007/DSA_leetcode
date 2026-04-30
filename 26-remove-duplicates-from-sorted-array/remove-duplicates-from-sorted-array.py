class Solution:
    def removeDuplicates(self, nums): 

        if not nums: 
            return "the list is empty"

        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]: 
                left += 1
                nums[left] = nums[right]

        return left + 1

nums = [0,0,1,1,1,2,2,3,3,4]

solution = Solution()
new_length = solution.removeDuplicates(nums)
print(f"the new length of the new list is : {new_length},                                                       and {nums[:new_length]} is the new list, without duplicates.")