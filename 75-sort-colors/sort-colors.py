class Solution:
    def sortColors(self, nums): 
        low = 0
        mid = 0
        high = len(nums) - 1 # here we are using three pointers 
        while mid <= high: 
            # we are using mid and high because that will be checking the 2nd last portion of the list that we are given, and we are using the <= because if we used < there will be one element left in the list to be sorted
            if nums[mid] == 0: # if 0 then we would have to left shift it coz we want it in the farthest left point
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1: # no change because that it its intended position
                mid += 1
            else: # nums[mid] == 2
            # here we would have to put it in the farthest right position of the list 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1 #here we are not incrementing the mid because the change that we did has not been checked yet and it is unsafe to increment without checking so it will process again

nums = [2,0,2,1,1,0]
solution = Solution()

solution.sortColors(nums)
print(nums) # done because no return element in the code, have to print the changed array 
