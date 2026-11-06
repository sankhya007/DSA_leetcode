class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # n = len(s) # will nto work because we need to keep in mind the senquence as well

        # count = 0 
        # for ch in s: 
        #     if ch in t: 
        #         count += 1
        #     else: 
        #         return False

        # return n == count


        i = 0 

        for ch in t: 
            # to keep the sequence we need to match the sequence once the sequence gets fucked we return false
            if i < len(s) and ch == s[i]: 
                i += 1

        return i == len(s)