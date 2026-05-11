class Solution(): 
    def reverseString(self, s): 
        left = 0
        right = len(s) - 1 
        while left < right:     
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
s = "what the fuck is wrong with the job market"
sentence = list(s)
solutoin = Solution()
print(solutoin.reverseString(sentence))