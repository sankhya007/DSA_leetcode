# check for anagram 

class Solution(): 
	def isAnagram(self, s1, s2): 
		return sorted(s1) == sorted(s2)

string1 = "tea"
string2 = "ate"
solution = Solution()
print(solution.isAnagram(string1, string2))