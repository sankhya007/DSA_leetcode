# car fleet - leetcode
# count the umber car that have the same fleet 

class Solution(): 
    def carFleet(self, target, position, speed): 

        # combine position alongside the speed in ascending order
        pairs = sorted(zip(position, speed), reverse=True)

        # storage
        stack = []

        for pos, spd in pairs: 

            # distance / speed
            time = (target - pos)/ spd 
            stack.append(time)

            # length of the stack has to be more than two because or else we can not do the comparison
            # and if the last car took less time than the previous one to reach there then it can speed up and join the previous car - then pop, but if it is slow then it can never join in and joins a seperate fleet - let it stay in stack
            # only the seperate fleet once stay in the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)