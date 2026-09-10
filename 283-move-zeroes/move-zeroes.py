# move zero - leetcode 

class Solution(): 
	def moveZeroes(self, nums): 

		# increment variable
		position = 0 

		# initial loop
		for num in nums: 

			# if value, accept, place next to each. one after another. when zero do nothing
			if num != 0: 
				nums[position] = num
				position += 1

		# till we reach the length, keep placing zero.
		while position < len(nums): 
			nums[position] = 0 
			position += 1 

		return nums

nums = [1,2,3,0,0,4,5,0,0,6,7]

sol = Solution()
print(sol.moveZeroes(nums))