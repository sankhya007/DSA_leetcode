from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:

        available = Counter(chars)
        total_length = 0 

        for word in words: 
            need = Counter(word)
            if all(need[c] <= available[c] for c in need): 
                total_length += len(word)

        return total_length