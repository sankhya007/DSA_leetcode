# class Solution(object):
#     def findPeakElement(self, nums):
#         peek = max(nums)

#         for i, num in enumerate(nums): 
#             if num == peek: 
#                 return i


# fnds the peek without scanning the entire array
class Solution(): 
    def findPeakElement(self, nums): 

        # pointers
        left = 0 
        right = len(nums) - 1

        # initial loop
        while left < right: 
            mid = (left + right) // 2 

            # if the mid is bigger than the mid + 1 then the peek should be at the left side of the array, because if the next number is small that means the number is gradually decreasing
            if nums[mid] > nums[mid + 1]: 
                right = mid

            else: 
                left = mid + 1 

        return left