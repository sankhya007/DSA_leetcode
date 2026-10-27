class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        big1  = big2 = 0 
        small1 = small2 = float("inf")

        for x in nums: 
            if x > big1: 
                big1, big2 = x, big1
            elif x > big2: 
                big2 = x

            if x < small1: 
                small1, small2 = x, small1
            elif x < small2:
                small2 = x 
        
        # placement in array (big1, big2,....., small1, small2)
        return big1 * big2 - small1 * small2