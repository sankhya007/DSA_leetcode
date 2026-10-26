class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1 

        # skip any spaces that is in the lst of the sentence
        while i >= 0 and s[i] == " ": 
            i -= 1 
        # this will stop when we hit a letter

        # if there is letter in the end of the sentence count
        length = 0 
        while i >= 0 and s[i] != " ": 
            length += 1
            i -= 1
        # this will stop when we hit a space

        return length