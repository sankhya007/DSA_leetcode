class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0 

        for i, t in enumerate(tickets): 
            # include who ever has minimum time left 
            # if the t is less than k then it will end before k 
            # if t is heigher than k then it'll not go after k is done, so we take k
            if i <= k: 
                time += min(t, tickets[k])

            # they will have one less round becase k itself will buy in that round
            else: 
                time += min(t, tickets[k] - 1)

        return time