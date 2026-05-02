class Solution:
    def rotate(self, nums, k): 
        k = k % len(nums) # if teh value of the k is higher than the length of the list
        self.reverse(nums, 0, len(nums) - 1) # reverse the whole array 
        self.reverse(nums, 0, k - 1) # reverse till k'th index or the 1st half
        self.reverse(nums, k, len(nums) - 1) # reverse the 2nd half of the reversed array

    def reverse(self, nums, start, end): # helping use reverse
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

nums = [1,2,3,4,5,6,7]
k = 3

solution = Solution()
solution.rotate(nums, k)
print(nums) # coz no return 