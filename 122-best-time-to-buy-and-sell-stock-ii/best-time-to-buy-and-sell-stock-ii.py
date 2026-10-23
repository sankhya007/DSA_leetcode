class Solution(): 
    def maxProfit(self, prices): 
        profit = 0 

        # leave out the 1st one because we need to negate that from prices[i]
        # the 1st one is prices[i - 1]
        for i in range(1, len(prices)): 
            if prices[i] > prices[i - 1]:
                # add increment
                profit += prices[i] - prices[i - 1]

        return profit 