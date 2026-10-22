from math import gcd

class Solution(): 
    def subsequencePairCount(self, nums): 

        MOD = 10**9 + 7 # given in the question
        M = max(nums)

        # make the score card
        dp = [[0]*(M+1) for _ in range(M+1)]
        dp[0][0] = 1
        # because the question does not allow the condition of both of the baskets to be empty so we have to assign a value to that manually 

        '''
        there are 3 things that we can do to the number
        option 1: do not add that in any basket 
        option 2: add that in basket 1 
        option 3; add that in basket 2
        '''

        for x in nums: # option 1
            new = [row[:] for row in dp]
            # replicate the rows by "for row in dp"
            # replicate list "row[:]"

            # go through every element in the matrix
            for a in range(M + 1): 
                for b in range(M + 1): 
                    c = dp[a][b]
                    if c == 0: 
                        continue
                    # if the values are empty, continue

                    ga = gcd(a, x)
                    new[ga][b] = (new[ga][b] + c) % MOD

                    gb = gcd(b, x)
                    new[a][gb] = (new[a][gb] + c) % MOD
                    # MOD to make sure that it does not exceed the limit 

            dp = new 
            # replace the old scorecard with the new scorecard

        return sum(dp[g][g] for g in range(1, M+1)) % MOD
        # we can not start with 0 because the question's options does not allows both of the buckets to be empty at the same time
        # so start from 1, and go till max 
        # add diagonal numbers

