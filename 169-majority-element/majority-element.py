class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        required_len = len(nums) // 2
        nums.sort()
        return nums[required_len]