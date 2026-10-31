class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        num = 0 
        sign = "+"

        for i,ch in enumerate(s):
            if ch.isdigit(): 
                num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s) - 1: 
                if sign == "+": 
                    stack.append(num)
                elif sign == "-": 
                    stack.append(-num)
                elif sign == "*": 
                    stack.append(stack.pop() * num)
                elif sign == "/": 
                    stack.append(int(stack.pop() / num)) 
                
                sign = ch
                num = 0 
        # we do not do thee sum, we just the do the multiplication and division
        # for +ve character we insert it as +ve character, and for - we insert "-" before the character
        # we just do the * and /
        # then return sum of every number in stack
        return sum(stack)