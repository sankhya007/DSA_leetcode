class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        
        res = []

        for i, insider1 in enumerate(words): 
            for j , insider2 in enumerate(words): 
                if i != j and insider1 in insider2: 
                    res.append(insider1)
                    break

        return res