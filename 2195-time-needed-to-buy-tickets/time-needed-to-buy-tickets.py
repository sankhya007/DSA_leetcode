class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:

        time = 0 

        for i, t in enumerate(tickets): 

            # for the index that are smaller or equal to k they will add the minimum of the time stored in the index itself, k itself
            # because time an not go beyond k 
            # these are the index that are exclusively in the left side of k
            if i <= k: 
                time += min(t, tickets[k])

            # this is for te index that is on the right side of k, and because k is going to finish in the mid round everyone on the right will not be able to buy that one time completely
            else: 
                time += min(t, tickets[k] - 1)

        return time

tickets = [2,3,2]
k = 2

sol = Solution()
print(sol.timeRequiredToBuy(tickets, k))