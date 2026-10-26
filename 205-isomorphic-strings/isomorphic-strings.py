class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for a, b in zip(s, t): 

            if a in s_to_t and s_to_t[a] != b: 
                return False
            if b in t_to_s and t_to_s[b] != a: 
                return False

            # add b as the value of a in set 
            # add a ad the value of b in set 
            # compare - if not same, return False
            
            s_to_t[a] = b
            t_to_s[b] = a

        return True