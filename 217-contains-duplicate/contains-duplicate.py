class Solution: 
	def containsDuplicate(self, nums): 
		# create storage
		num_set = set()

		for num in nums: 
			# if exists return True
			if num in num_set: 
				return True
			# if not then add to set
			else: 
				num_set.add(num)

		# not exists so return False
		return False