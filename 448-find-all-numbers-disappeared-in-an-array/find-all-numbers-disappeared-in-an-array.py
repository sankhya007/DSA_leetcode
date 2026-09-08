class Solution: 
	def findDisappearedNumbers(self, nums): 

		# length and storage
		n = len(nums)
		num_set = set(nums)
		missing_number = []

		# only works because the missing ones are duplicates of others
		for num in range(1, n+1): 
			# if not found in num_set then append
			if num not in num_set: 
				missing_number.append(num)

		# display 
		return missing_number