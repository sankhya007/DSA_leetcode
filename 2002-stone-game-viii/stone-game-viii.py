# stone game VIII

from itertools import accumulate

class Solution(): 
    def stoneGameVIII(self, stones): 
        n = len(stones)
        prefix = list(accumulate(stones))

        # prefix is the already accumulated value
        # the best is the last element in prefix because that is the best-est possible way for the problem to be bypassed (that all of the stones are taken by the user, so the game ends right there)
        best = prefix[-1]

        # n-2 -> so we leave the last element and we continue towards 0
        # now when we do prefix[i] - best, meaning rather than alice getting all the stones bob is getting stones one by one 
        for i in range(n - 2, 0, -1): 
            best = max(best, prefix[i] - best)

        return best