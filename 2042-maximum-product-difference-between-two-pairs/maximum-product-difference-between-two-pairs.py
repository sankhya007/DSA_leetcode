class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums) - 1
        w = nums[0]
        x = nums[1]
        y = nums[length - 1]
        z = nums[length]

        return (y * z) - (w * x)