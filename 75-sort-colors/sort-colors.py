class Solution(object):
    def sortColors(self, nums):
        low = 0 
        mid = 0 
        high = len(nums) - 1

        while mid <= high:
            
            # go down
            if nums[mid] == 0: 
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # at the right place
            elif nums[mid] == 1: 
                mid += 1

            # go up
            else: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1