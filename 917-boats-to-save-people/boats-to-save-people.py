# boats to save people - leetcode 

class Solution(): 
	def numRescueBoats(self, people, limit): 

		people.sort()

		# pointers
		left = 0 
		right = len(people) - 1

		# boat number storage
		boats = 0 

		# initial loop
		while left <= right: 

			# can both the heaviest and the lightest person fit? 
			# yes -> move them together
			if people[left] + people[right] <= limit: 
				# left and right increment when both fit
				left += 1

			# no -> move only the heavy person
			# right increment every time, heaviest person will always fit in one 
			right -= 1 

			#boat number increment every loop 
			boats += 1

		return boats

people = [3,5,3,4]
limit = 5

sol = Solution()
print(sol.numRescueBoats(people, limit))
