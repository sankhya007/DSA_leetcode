class Solution(): 
    def carFleet(self, target, position, speed): 

        pairs = sorted(zip(position, speed), reverse = True)

        stack = []

        for pos, spd in pairs: 
            time = (target - pos)/spd
            stack.append(time)

            while len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)