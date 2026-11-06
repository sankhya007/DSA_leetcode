class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # stack = s.split()
        # return len(stack.pop())

        i = len(s) - 1 # this is the last index of the string
        length = 0 

        while i >= 0 and s[i] == " ": 
            i -= 1
        while i >= 0 and s[i] != " ": 
            length += 1
            i -= 1 
        
        return length