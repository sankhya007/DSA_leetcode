class Solution(): 
	def sortedSquares(self, nums): 

		for i, num in enumerate(nums):
			nums[i] = num*num

		nums.sort()

		return nums