class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern_to_s = {}
        s_to_pattern = {}

        words = s.split(" ")

        if len(pattern) != len(words): 
            return False

        for p, w in zip(pattern, words): 
            if p in pattern_to_s and pattern_to_s[p] != w: 
                return False

            if w in s_to_pattern and s_to_pattern[w] != p: 
                return False

            pattern_to_s[p] = w
            s_to_pattern[w] = p

        return True 