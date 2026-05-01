class Solution:
    def maxProfit(self, prices): 
        min_price = float("inf") # every number will be lower than this thats why infinity
        max_profit = 0 # every number will be bigger than this because then how can it be profit if it is in negative thats why it is zero 

        for price in prices: 
            if price < min_price: 
                min_price = price
            elif price - min_price > max_profit: 
                max_profit = price - min_price

        return max_profit
        
prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))