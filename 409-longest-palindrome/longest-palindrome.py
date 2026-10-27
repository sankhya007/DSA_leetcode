from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0 

        for c in s: 
            count[c] += 1
            # meaning even number, odd will not count
            # so at every even number we take 2 increment
            if count[c] % 2 == 0: 
                res += 2
        
        # the middle letter, if the res is full length meaning there is nothing that we can add, and if it is not that means that we can add another character
        return res + (res < len(s))