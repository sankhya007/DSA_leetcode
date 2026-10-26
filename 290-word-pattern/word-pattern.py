class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words): 
            return False

        # this is how it is going to be stored, litrally
        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words): 

            if c in char_to_word and char_to_word[c] != w: 
                return False
            if w in word_to_char and word_to_char[w] != c: 
                return False

            # we store then we check if it matches
            char_to_word[c] = w
            word_to_char[w] = c        

        return True 