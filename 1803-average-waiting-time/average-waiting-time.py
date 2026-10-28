class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        t = 0 
        total = 0 

        for arrival, order in customers: 
            # if greater add how much time that the person will have to wait before he can order
            if t > arrival: 
                total += t - arrival
            else: 
                t = arrival
            total += order
            t += order

        return total / len(customers)