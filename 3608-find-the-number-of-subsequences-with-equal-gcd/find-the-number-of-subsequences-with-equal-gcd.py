class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10**9 + 7 
        M = max(nums)

        dp = [[0]*(M+1) for _ in range(M+1)]
        dp[0][0] = 1
        
        for x in nums: 
            new = [row[:] for row in dp]

            for a in range(M+1): 
                for b in range(M+1): 
                    c = dp[a][b]
                    if c == 0: 
                        continue

                    ga = gcd(a, x)
                    new[ga][b] = (new[ga][b] + c) % MOD

                    gb = gcd(b, x)
                    new[a][gb] = (new[a][gb] + c) % MOD

            dp = new

        return sum(dp[g][g] for g in range(1, M+1)) % MOD


        