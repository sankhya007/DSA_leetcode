class Solution(): 
	def guessNumber(self, n): 

		left = 1 
		right = n 

		while left <= right: 

			mid = (left + right) // 2 

			# guess is nothing but a predefined function
			result = guess(mid)

			# following is the working principal of guess
			if result == 0: 
				return mid

			elif result == -1: 
				right = mid - 1

			else: 
				left = mid + 1
			

# this does not even make any fucking sense