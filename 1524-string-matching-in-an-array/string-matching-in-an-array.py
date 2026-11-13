class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:

        array = []
        for i in range(len(words)): 
            for j in range(len(words)): 
                if i != j and words[i] in words[j]: 
                    array.append(words[i])
                    break

        return array