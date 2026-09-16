# daily temp

class Solution(): 
    def dailyTemperatures(self, temperatures): 

        # storage to store the days in 
        n = len(temperatures)
        storage = [0] * n 

        # empty stack for temp storage of index
        stack = []

        for i, temp in enumerate(temperatures): 

            # if value in stack, and today's temp more than yesterday's temp
            while stack and temp > temperatures[stack[-1]]: 

                # assign yesterday's index
                prev_index = stack.pop()

                # i = current index, prev_index = last index which was more than today
                # storing how much more 
                storage[prev_index] = i - prev_index

            # store index to compare
            stack.append(i)

        return storage

