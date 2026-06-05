class Solution(): 
    def reverseWords(self, s): 
        seperated = s.split()
        reverse = seperated[::-1]
        return " ".join(reverse)