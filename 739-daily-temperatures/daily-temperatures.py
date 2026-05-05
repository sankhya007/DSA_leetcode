class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n # this is to get the answer array the same length as the given array that we have to process
        stack = []

        for i, temp in enumerate(temperatures): # here we are using enumarate to see what we actually getfrom the tempratures in a set 
            while stack and temp > temperatures[stack[-1]]: # here we are seeing if the next temp in the given temoratures are bigger than the previous temp or no because we added that in the last line of the while loop 
                prev_index = stack.pop() # pop the top most elemenet in the stack 
                answer[prev_index] = i - prev_index # and here we are using the undex of the given list to store the vals of the list in the previous index and also i - prev index to get the difference 
            stack.append(i) # no matter what we have to append the index of the ongoing temprature to the stack, if the next temp is always bigger then we just have one element in the stack and f the next temp is smaller than prev elemenet then we just add the index in the stack so then stack has more than one variables 

        return answer
