class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
         
        stack = []

        for i, p in enumerate(prices): 
            while stack and prices[stack[-1]] >= p: 
                prices[stack.pop()] -= p
            stack.append(i)
        return prices