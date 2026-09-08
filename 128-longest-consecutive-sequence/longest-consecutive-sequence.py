class Solution: 
	def longestConsecutive(self, nums): 
		num_set = set(nums)
		longest = 0 

		for num in num_set: 

			# check if sequence is there
			if num - 1 not in num_set: 
				length = 1 # if not then no change to addition

				# if the addition is there then try +1, keep going..
				while num + length in num_set: 
					length += 1 

				# find the longest thread of numbers
				longest = max(length, longest)

		return longest
