class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:

        l = 0 # left pointer 
        window = max_window = 0 # non satisfied customers
        satisfied = 0 # satisfied customer count 

        # the shop is open for n minutes, n = len(customers)
        for r in range(len(customers)): 
            # r = right pointer
            # add corresponding value in the assigned locations 
            if grumpy[r]: # meaning grumpy = 1
                window += customers[r] 
            else: # grumpy = 0 
                satisfied += customers[r]

            # minutes is the given time the owner can stay non grumpy but only once throughout the open time
            # sliding window
            if r - l + 1 > minutes:
                if grumpy[l]: # and if the left point the owner was grumpy we have to negate that form the total counter
                    window -= customers[l] 
                l += 1 # left pointer move forward because the window (r - l + 1) is bigger than intended(minutes)

            max_window = max(window, max_window)

        '''
        1. satisfied is the number of customer that are already satisfied
        2. window is the number of customer that are unsatisfied 
        3. we try to negate the number of people that we can not help because of the given restrictions, from the window 
        4. retract the max value form that and add that to the satisfied customer count
        '''

        return satisfied + max_window




customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

sol = Solution()
print(sol.maxSatisfied(customers, grumpy, minutes))