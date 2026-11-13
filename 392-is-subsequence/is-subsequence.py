class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0 
        
        for ch in t: 
            if pointer < len(s) and ch == s[pointer]: 
                pointer += 1

        return pointer == len(s)