# container with most water - leetcode

class Solution(): 
	def maxArea(self, heights): 

		# pointers
		left = 0 
		right = len(heights) - 1

		# storage
		max_area = 0 

		# initial loop 
		while left < right: 

			# container bottom width 
			containter_width = right - left

			# will be changing for each columns till none left
			variable_area = min(heights[left], heights[right]) * containter_width

			# will capture only the max 
			max_area = max(max_area, variable_area)

			# trying to match up the smaller left with bigger right, by left increment
			if heights[left] < heights[right]: 
				left += 1 

			# right increment
			else: # right < left
				right -= 1

		return max_area