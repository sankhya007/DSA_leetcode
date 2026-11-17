class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0 
        mid = 0 
        high = len(nums) - 1

        # so basically there are three things that can happen the mid can be either 0, 1 or 2
        # and for those 3 moments we have 3 things that we can do 
        # when mid is 0 swap it with low
        # when mid is 1 that means it is in the correct position
        # and when mid is 2 swap it with high

        # this is a 3 pointer tactic
        # low and mid are starting form the start of the array that is why when we swap them or do anything to them we append 1 
        # and because high is starting from the right side of the array we decrement the value

        while mid <= high: 
            if nums[mid] == 0: 
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1: 
                mid += 1
                # this is the only point where the mid pointer gains the access to move forward than low
        
            else: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1