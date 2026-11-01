import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles) 
        res = right # this is the max bananas koko can eat even if he can eat more than this that will not cause any result in the output 

        while left <= right: 
            k = left + (right - left) // 2
            hour = 0 

            for pile in piles: 
                hour += math.ceil(pile / k)

            if hour <= h: 
                res = min(res, k)
                right = k - 1
            
            else: 
                left = k + 1

        return res