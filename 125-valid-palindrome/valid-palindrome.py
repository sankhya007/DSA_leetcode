class Solution():
    def isPalindrome(self, s):

        left = 0 
        right = len(s) - 1

        while left < right: 
            # if it is a number or letter it will return true, anything else(space, special characters) will return false so we can skip past that
            # not alpha numeric means anything else but alphabet and neumericals
            while left < right and not s[left].isalnum(): 
                left += 1

            while left < right and not s[right].isalnum(): 
                right -= 1 

            # because it is not case sensitive
            while s[left].lower() != s[right].lower(): 
                return False

            # else case, where we meet the requirements
            left += 1 
            right -= 1

        return True 
            
