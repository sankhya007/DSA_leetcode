# trapped rain water - leetcode 

class Solution():
	def trap(self, height): 

		# in case list empty
		if not height: 
			return 0 

		# two pointers
		left = 0 
		right = len(height) - 1

		# max pointers 
		max_left = 0 
		max_right = 0 

		# storage 
		trapped_water = 0 

		# starting sequence 
		while left < right: 

			# calculation sequence if the left height bigger top code block will run, else bottom block 

			# top block
			if height[left] < height[right]: 

				# if left column bigger than initial left, store 
				if height[left] >= max_left: 
					max_left = height[left]

				# total amount of water
				else: 
					trapped_water += max_left - height[left]

				# increment
				left += 1 

			# bottom block
			else: 

				# if right column bigger than initial right, store
				if height[right] >= max_right: 
					max_right = height[right]

				# total water captured 
				else: 
					trapped_water += max_right - height[right]

				# increment 
				right -= 1 

		return trapped_water


heights = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap(heights))

