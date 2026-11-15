from collections import defaultdict

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        freq = defaultdict(int)
        
        for word in words: 
            for ch in word: 
                freq[ch] += 1

        for i, ch in freq.items(): 
            if ch % len(words): 
                return False

        return True