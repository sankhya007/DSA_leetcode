from collections import defaultdict

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        freq = defaultdict(int)
        
        for word in words: 
            for ch in word: 
                freq[ch] += 1

        for ch in freq: 
            if freq[ch] % len(words) != 0: 
                return False

        return True