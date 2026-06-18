class Solution: 
    def dailyTemperatures(self, tempratures): 
        n = len(tempratures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(tempratures): 
            while stack and temp > tempratures[stack[-1]]: 
                prev_index = stack.pop() # pop last value
                answer[prev_index] = i - prev_index # value of specified index
            stack.append(i) # append if nothing exits
        return answer