class Solution(): 
    def rob(self, nums): 

        prev2 = 0 # money count of 2 houses back
        prev1 = 0 # money count till the last house

        for money in nums: 
            current = max(prev1, prev2+money)
            prev2 = prev1
            prev1 = current
            # sliding window - increment

        return prev1
        # this will be the max value
