class Solution:
    def reverseWords(self, s): 
        devided_str = s.split()
        reversed_str = devided_str[::-1]
        return " ".join(reversed_str)

string = "nigga man"
solution = Solution()
print(solution.reverseWords(string))
        