class Solution(): 
	def reverseOnlyLetters(self, s):
		s = list(s)
		left = 0 
		right = len(s) - 1

		while left < right: 
			# this portion of the code is written so then it is going to skip the non alphaneumaric characters in the input
			if not s[left].isalpha(): 
				left += 1
			elif not s[right].isalpha(): 
				right -= 1
			# this is the reverse logic of the code
			else:
				s[left], s[right] = s[right], s[left]
				left += 1
				right -= 1

		return "".join(s)

string = "sankhya"
solution = Solution()
print(solution.reverseOnlyLetters(string))
		