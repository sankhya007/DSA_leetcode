class Solution(): 
    def carFleet(self, target, position, speed): 

        pairs = sorted(zip(position, speed), reverse = True)

        stack = []

        for pos, spd in pairs: 
            time = (target - pos)/spd
            stack.append(time)

            # len(stack) >= 2 because it needs two cars to compare
            # stack[-1] is last element 
            # stack[-2] is the 2nd last element
            # element is time, so if time less means they can catch up 
            # if they can catch up pop, if they can not stay
            while len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)