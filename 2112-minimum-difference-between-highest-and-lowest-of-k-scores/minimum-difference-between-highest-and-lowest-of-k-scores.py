class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        minimum = float('inf')
        nums.sort()
        # because we are using k as an index, negate 1 from it becasue in python index starts form 0 and not 1
        for i in range(k - 1 , len(nums)):
            difference = nums[i] - nums[i - (k - 1)]
            minimum = min(minimum, difference)

        return minimum