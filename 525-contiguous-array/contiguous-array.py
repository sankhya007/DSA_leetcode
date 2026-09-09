class Solution(): 
	def findMaxLength(self, nums): 

		# storage
		prefix_sum = {0: -1}
		current_sum = 0 
		max_length = 0 

		for i, num in enumerate(nums): 

			# seeing scheme 
			if num == 0: 
				current_sum -= 1
			else: 
				current_sum += 1

			# if visible, calculate length 
			if current_sum in prefix_sum: 
				# i = current position 
				# prefix_sum[current_sum] = last seen position 
				length = i - prefix_sum[current_sum]
				max_length = max(length, max_length)

			# if not visible, just add
			else: 
				prefix_sum[current_sum] = i

		return max_length

nums = [0,1,1,1,1,1,0,0,0]

solution = Solution()
print(solution.findMaxLength(nums))