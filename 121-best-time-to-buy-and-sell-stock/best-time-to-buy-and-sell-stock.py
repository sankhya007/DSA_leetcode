# best time to buy and sell stock 

class Solution(): 
    def maxProfit(self, prices): 

        max_profit = 0 
        min_price = float("inf")
        # cant be bigger than this

        for price in prices: 
            if price < min_price: 
                min_price = price
                # min price is the lowest we have seen

            # will find the max difference
            elif price - min_price > max_profit: 
                max_profit = price - min_price

        return max_profit

prices = [7,1,5,3,6,4]

sol = Solution()
print(sol.maxProfit(prices))