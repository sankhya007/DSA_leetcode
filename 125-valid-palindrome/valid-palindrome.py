class Solution():
    def isPalindrome(self, s):

        # sliding window
        left = 0 
        right = len(s) - 1

        while left < right: 
            # check alphaneumaric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum(): 
                right -= 1

            # check simillarity
            while s[left].lower() != s[right].lower(): 
                return False 

            left += 1
            right -= 1
            # incremental increase

        return True