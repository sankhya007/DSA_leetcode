class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = max_count = 0 
        for i in range(len(nums)): 
            if nums[i] == 1: 
                count += 1
            elif nums[i] == 0: 
                count = 0 

            max_count = max(count, max_count)

        return max_count