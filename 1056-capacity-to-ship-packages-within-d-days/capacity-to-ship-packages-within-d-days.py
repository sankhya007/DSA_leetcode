import math
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right: 

            capacity = left + (right - left) // 2

            current_weight = 0 
            day_count = 1

            for weight in weights: 
                if current_weight + weight > capacity: 
                    current_weight = 0 
                    day_count += 1

                current_weight += weight

            if day_count <= days: 
                right = capacity - 1

            else: 
                left = capacity + 1

        return left
            