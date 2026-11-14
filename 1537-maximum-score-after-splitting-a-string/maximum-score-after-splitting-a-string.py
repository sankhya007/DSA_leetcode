class Solution:
    def maxScore(self, s: str) -> int:
        onces = s.count("1")
        zeros = 0 
        best = 0 

        for i in range(len(s)-1): 
            if s[i] == "0": 
                zeros += 1
            else: 
                onces -= 1
            
            best = max(best, zeros+onces)

        return best