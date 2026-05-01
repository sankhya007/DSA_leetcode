class Solution:
    def findMin(self, nums): 
        left = 0 
        right = len(nums) - 1  
        while left < right: 
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: 
                left = mid + 1
            else: # nums[mid] < nums[left]
                right = mid
        return nums[right]
nums = [3,4,5,1,2]
solution = Solution()
print(solution.findMin(nums))