from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
    
        n = len(stones)
        prefix = list(accumulate(stones))

        best = prefix[-1]

        for i in range(n-2, 0, -1): 
            best = max(best, prefix[i] - best)

        return best