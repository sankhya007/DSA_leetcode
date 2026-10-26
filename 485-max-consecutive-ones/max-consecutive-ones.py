class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        best = 0 
        length = 0 

        for i in nums: 
            if i == 1: 
                length += 1 
                best = max(best, length)
            else: 
                length = 0  # reset back when hit 0

        return best