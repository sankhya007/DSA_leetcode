class Solution:
    def minOperations(self, s: str) -> int:
        mismatches = 0 

        for i, ch in enumerate(s): 
            expected = "0" if i % 2 == 0 else "1"
            if ch != expected:
                mismatches += 1

        return min(mismatches, len(s) - mismatches)
                