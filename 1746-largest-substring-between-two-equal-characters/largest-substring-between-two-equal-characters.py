class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        first_index = {}
        last_index = {}

        for i, c in enumerate(s):
            if c not in first_index: 
                first_index[c] = i
            else: 
                last_index[c] = i

        for c in last_index: 
            res = max(res, last_index[c] - first_index[c] - 1)

        return res