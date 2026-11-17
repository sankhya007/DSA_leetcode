class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        #[arrival time, time taken]
        t = 0 
        total = 0 

        # assuming that t is the current time, so if the customer arrives and the arrival is lower than the current time that means the customer would have to wait
        # else current time just becomes that arrival time which is telling us that the person was waiting for a while before customer showed up
        
        for arrival, order in customers: 
            if t > arrival: 
                total += t - arrival
            else: 
                t = arrival
            total += order
            t += order

        return total / len(customers)