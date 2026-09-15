# find minimum in rotated array 

class Solution(): 
	def findMin(self, nums): 

		# pointers
		left = 0 
		right = len(nums) - 1

		# initial loop 
		while left < right: 

			mid = left + (right - left) // 2 

			# write it down it will make more sense 
			if nums[mid] > nums[right]: 
				left = mid + 1 

			else: 
				right = mid 

		return nums[right]

nums = [4,5,6,7,0,1,2]

sol = Solution()
print(sol.findMin(nums))