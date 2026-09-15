# first bad version 

class Solution(): 
	def firstBadVersion(self, n): 

		# run from 1 to n 
		left = 1 
		right = n 

		# initial loop
		while left < right:
			
			# find mid 
			mid = left + (right - left) // 2

			# if returns true, right side corrupted
			if isBadVersion(mid): 
				right = mid 

			# if returns false, left side all good. in right find the starting bad one
			else: 
				left = mid + 1 

		return left 