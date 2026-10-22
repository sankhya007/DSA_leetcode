# best time to buy and sell stock 

class Solution(): 
    def maxProfit(self, prices): 

        max_profit = 0 
        min_price = float("inf") # basically infinity

        for price in prices: 

            if price < min_price: 
                min_price = price
                # determine the lowest price

            elif price - min_price > max_profit: 
                max_profit = price - min_price
                # determine the max price

        return max_profit