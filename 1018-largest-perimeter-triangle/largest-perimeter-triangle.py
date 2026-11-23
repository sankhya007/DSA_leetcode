class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1, 1, -1): # stop at 1 because we also need i-1 and i-2
            largest = nums[i] 
            middle = nums[i-1] 
            smallest = nums[i-2] 

            if smallest + middle > largest: 
                return smallest + middle + largest

        return 0