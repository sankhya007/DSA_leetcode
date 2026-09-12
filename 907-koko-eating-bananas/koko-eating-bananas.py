# koko eating bananas - leetcode 

class Solution(): 
	def minEatingSpeed(self, piles, h): 

		# at mean can have one banana one hr 
		left = 1 
		# at max can eat the whole pile in one hr 
		right = max(piles)

		# loop 
		while left <= right: 

			# trying out the mid speed 
			k = (left + right) // 2  

			# container
			hours = 0 

			for pile in piles: 
				# calculate rounded up
				hours += (pile + k - 1) // k 

			# no need to increment or decrement left, right. that makes the process slower. jump to the value of K that is better for the calculation
			# if k is sufficient, find if possible slower
			if hours <= h: 
				right = k - 1
				# right -= 1

			# if not sufficient, find if possible faster
			else: 
				left = k + 1 
				# left += 1
				
		return left

piles = [3,6,7,11] 
h = 8

sol = Solution()
print(sol.minEatingSpeed(piles, h))