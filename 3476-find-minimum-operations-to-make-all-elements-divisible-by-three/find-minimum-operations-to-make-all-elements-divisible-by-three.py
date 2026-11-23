class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0 
        for i in range(len(nums)): 
            if nums[i] % 3 != 0: 
                left_outs = min(nums[i] % 3, 3 - (nums[i] % 3))
                total += left_outs
        return total