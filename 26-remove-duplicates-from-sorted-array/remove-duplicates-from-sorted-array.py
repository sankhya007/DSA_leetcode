class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if not nums: 
            return "empty list"

        left = 0 
        for right in range(0, len(nums)): 
            # if they do not match, left increments and right becomes left 
            if nums[left] != nums[right]: 
                left += 1
                nums[left] = nums[right]
        return left + 1