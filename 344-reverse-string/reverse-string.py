class Solution(): 
    def reverseString(self, s): 
        left = 0
        right = len(s) - 1 
        while left < right: 
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # checking of the sync works 

s = "nigga"
string = list(s)
solution = Solution()
print(solution.reverseString(string))