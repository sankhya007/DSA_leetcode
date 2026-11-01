class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        minimum = float('inf')
        nums.sort()
        for i in range(k - 1 , len(nums)):
            difference = nums[i] - nums[i - (k - 1)]
            minimum = min(minimum, difference)

        return minimum