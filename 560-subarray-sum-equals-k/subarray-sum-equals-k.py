class Solution(): 
	def subarraySum(self, nums, k): 
		count = 0 
		current_sum = 0 
		prefix_sum = {0:1}

		for num in nums: 
			current_sum += num # addition happens one by one(every number gets added)

			# current_sum - k is the number we need to get to k 
			if current_sum - k in prefix_sum: # is that number in prefix_sum ? 
				count += prefix_sum[current_sum - k] # if exists then add that 

			prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1 # keeping track of how many times it appeared in the array
			# prefix_sum(current_sum, 0) - is the current)_sum in the prefix_sum? if so return the number and if not then return 0 
			# add one because it was visible one more time

		return count