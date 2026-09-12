# binary search - leetcode 

class Solution(): 
	def search(self, nums, target): 

		# pointers
		left = 0 
		right = len(nums) - 1

		# initial loop 
		while left <= right: 

			# find mid
			middle = (left + right) // 2 

			# if match return middle
			if nums[middle] == target: 
				return middle 

			# if small left increment
			elif nums[middle] < target: 
				left = middle + 1 

			# if big right increment
			else: 
				right = middle -1 

		# if no match
		return -1 

nums = [1,2,3,4,5,6,7,8,9]
target = 4

sol = Solution()
print(sol.search(nums,target))