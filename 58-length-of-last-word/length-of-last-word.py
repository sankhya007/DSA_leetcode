class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0 
        loop_len = len(s) - 1
        
        while loop_len >= 0 and s[loop_len] == " ": 
            loop_len -= 1

        while loop_len >= 0 and s[loop_len] != " ": 
            count += 1
            loop_len -= 1

        return count
