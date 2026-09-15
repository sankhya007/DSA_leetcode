class Solution(object):
    def searchInsert(self, nums, target):
        
        # pointers
        left = 0 
        right = len(nums) - 1

        while left <= right: 

            mid = left + (right - left) // 2 

            if nums[mid] == target: 
                return mid

            elif nums[mid] < target: 
                left = mid + 1 

            else: 
                right = mid - 1

        # find the place where it should be
        return left 

nums = [1,3,5,6]
target = 2

sol = Solution()
print(sol.searchInsert(nums, target))