from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        freq = Counter(nums)

        for count in freq.values(): 
            # look for mishap, not the correct in code
            if count % 2 != 0:
                return False
        
        return True