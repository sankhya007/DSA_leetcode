# capacity to ship packages within D days 

class Solution():
    def shipWithinDays(self, weights, days):
        
        left = max(weights)
        right = sum(weights)

        while left <= right: 

            # mid of the left and right
            capacity = left + (right - left) // 2 

            # starting 
            current_weight = 0 # can have no goods 
            required_days = 1 # has to be day 1 

            # initial loop 
            for weight in weights: 

                # if capacity exceeds, days + 1. current_weight resets
                if current_weight + weight > capacity: 
                    required_days += 1 
                    current_weight = 0 

                # else current_weight adds to it existing, in the same day
                current_weight += weight 

            # if count is less try with less capacity in a day so you have less to carry, and can have more days
            if required_days <= days: 
                right = capacity - 1 

            # if day more, increase capacity
            else: 
                left = capacity + 1 

        return left 


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

sol = Solution()
print(sol.shipWithinDays(weights, days))