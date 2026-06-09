class Solution(): 
    def rotate(self, nums, k): 
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1) #1st half
        self.reverse(nums, k, len(nums) - 1) #2nd half
    def reverse(self, nums, start, end): 
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    