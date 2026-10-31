class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left = 0 
        right = len(nums) - 1
        res = [pivot] * len(nums)

        for i in range(len(nums)): 
            j = len(nums) - 1 - i
            if nums[i] < pivot: 
                res[left] = nums[i]
                left += 1
            if nums[j] > pivot: 
                res[right] = nums[j]
                right -= 1

        return res
