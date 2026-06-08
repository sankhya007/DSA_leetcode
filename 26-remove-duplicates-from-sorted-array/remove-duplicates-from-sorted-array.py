class Solution:
    def removeDuplicates(self, nums): 
        if not nums: 
            return "empty array"
        left = 0 
        for right in range(0, len(nums)): 
            if nums[left] != nums[right]: 
                left += 1
                nums[left] = nums[right]
        return left + 1
