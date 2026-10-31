class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0 
        right = len(nums) - 1
        array = []

        while left <= right: 
            if abs(nums[left]) < abs(nums[right]): 
                array.append(nums[right] * nums[right])
                right -= 1
            else: 
                array.append(nums[left] * nums[left])
                left += 1

        return array[::-1]

