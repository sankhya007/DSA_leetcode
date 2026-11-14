from collections import Counter

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        available = set(allowed)   
        count = 0

        for word in words: 
            if all(c in available for c in word): 
                count += 1

        return count