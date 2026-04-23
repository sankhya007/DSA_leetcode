class Solution():
	def rotateString(self, s, goal): 
		# if the string is not the same length then how can it qualify for the question 
		if len(s) != len(goal):
			return False 

		return goal in s + s

string = "abcde"
goal = "deabc"
sol = Solution()
print(sol.rotateString(string, goal))