from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        
        max_odd = max(f for f in freq.values() if f % 2 == 1)
        max_even = min(f for f in freq.values() if f % 2 == 0)

        return max_odd - max_even