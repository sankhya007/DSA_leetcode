from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        need = Counter(ransomNote)

        return all(need[c] <= available[c] for c in need)