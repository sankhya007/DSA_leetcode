from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        res = 0 

        for ch in s: 
            freq[ch] += 1

            if freq[ch] % 2 == 0: 
                res += 2

        return res + (res < len(s))