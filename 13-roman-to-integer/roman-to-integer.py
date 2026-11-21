class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        res = 0 
        for i in range(len(s)): 
            # if we are not at the last element and the current roman element is smaller than the next roman element so then remove the current element from the total and then when we add the next roman in whole that will be stabilized
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]: 
                res -= roman[s[i]]
            else: 
                res += roman[s[i]]

        return res