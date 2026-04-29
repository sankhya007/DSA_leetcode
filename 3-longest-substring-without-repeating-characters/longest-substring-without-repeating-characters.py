# print the longest substring without repeating characters 
class Solution(): 
	def lengthOfLongestSubstring(self, s):
		storage = set()
		left = 0 # left starts with the 0th point and the right is looped
		max_length = 0 #this is something we are going to test at each step

		for right in range(len(s)): 
			while s[right] in storage: 
				storage.remove(s[left]) # remove the value of the left var		
				left += 1
			storage.add(s[right])
			max_length = max(max_length, right - left + 1)
		
		return max_length

string = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(string))
		