class Solution(): 
	def missingNumber(self, nums): 
		n = len(nums)
		# this is just how it is, this is the way to do it
		expected_sum = n * (n + 1) // 2
		# we have to start with 0 
		actual_sum = sum(nums)
		return expected_sum - actual_sum
