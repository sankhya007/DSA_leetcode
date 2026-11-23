class Solution:
    def average(self, salary: list[int]) -> float:
        min_ammount = float("inf")
        max_ammount = -1
        total, custom_total = 0, 0 
        custom_length = len(salary) - 2
        
        for money in salary: 
            total += money 
            min_ammount = min(min_ammount, money)
            max_ammount = max(max_ammount, money)

        custom_total = total - max_ammount - min_ammount
        return custom_total / custom_length