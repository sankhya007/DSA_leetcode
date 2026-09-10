# class Solution(): 
# 	def sortedSquares(self, nums): 
# 		for i, num in enumerate(nums):
# 			nums[i] = num*num
# 		nums.sort()
# 		return nums

# time complexity O(n log n) ^


class Solution(): 
	def sortedSquares(self, nums): 

		# pointers
		left = 0 
		right = len(nums) - 1

		# storage
		result = [0] * len(nums)

		# start from end
		position = len(nums) - 1

		# initial loop
		while left <= right: 

			# absolute value because when sq "+ve" value or "-ve" value doesn't really matter
			# left > right, coz coming from backwards
			if abs(nums[left]) > abs(nums[right]): 
				result[position] = nums[left] ** 2
				left += 1

			# abs(nums[right]) > abs(nums[left])
			else: 
				result[position] = nums[right] ** 2 
				right -= 1

			# next variable
			position -= 1

		return result

# time complexity O(n)