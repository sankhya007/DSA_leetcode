# searching rotated sorted array - leetcode 

class Solution(): 
	def search(self, nums, target): 

		# ponters 
		left = 0
		right = len(nums) - 1

		# initial loop 
		while left <= right:

			# mid calculation (find the middle, add that to the position of left pointer)
			mid = left + (right - left) // 2

			# if match return
			if target == nums[mid]: 
				return mid

			# left smaller than mid
			elif nums[left] <= nums[mid]:

				# check if between left and mid, if so increment right 
				if nums[left] <= target < nums[mid]: 
					right = mid - 1
				# else increment left
				else: 
					left = mid + 1 

			# right smaller than mid
			else: 

				# check if between mid and right, if so increment left
				if nums[mid] < target <= nums[right]: 
					left = mid + 1
				# else right increment 
				else: 
					right = mid - 1

		# no trace found - return -1
		return -1 


sol = Solution()

nums = [4,5,6,7,0,1,2]
target = 0

print(sol.search(nums, target))