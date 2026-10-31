class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        def join(word): 
            string = ""
            for char in word: 
                string += char
            return string

        result1 = join(word1)
        result2 = join(word2)

        return result1 == result2