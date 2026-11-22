class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0 
        for account in accounts: 
            total_value = 0 
            for cash in account: 
                total_value += cash
            max_wealth = max(max_wealth, total_value)

        return max_wealth