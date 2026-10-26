from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:

        # use Counter because we also have to worry about the number of lettes that we have in the given string, also compare that
        available = Counter(chars)
        total_length = 0 

        for word in words: 
            need = Counter(word)
            if all(need[c] <= available[c] for c in need):
                total_length += len(word)

        return total_length

            