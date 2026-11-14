from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        need = Counter(ransomNote)

        if all(need[c] <= available[c] for c in need): 
            return True

        return False