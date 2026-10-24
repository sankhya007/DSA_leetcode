class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1) # full reverse 
        self.reverse(nums, 0, k-1) # 1st half reverse 
        self.reverse(nums, k, len(nums) - 1) # 2nd half reverse
        
    def reverse(self, nums, start, end): 
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1