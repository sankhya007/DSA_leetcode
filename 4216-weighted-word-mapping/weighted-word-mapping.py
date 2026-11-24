class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        string = ""
        for word in words: 
            total = 0 
            index = 0 
            for ch in word: 
                value = weights[ord(ch) - ord('a')]
                total += value
            index = total % 26 
            string += chr(ord('a') + 26 - index - 1)
        return string