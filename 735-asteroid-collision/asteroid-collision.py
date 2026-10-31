class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids: 
            # a has to be a negitivi for the while loop to work
            while stack and a < 0 < stack[-1]: 
                if stack[-1] < -a: # smaller one explode and bigger one stays
                    stack.pop()
                    continue # do the while again, keep going untill the negitive one alive
                elif stack[-1] == -a: # both explode
                    stack.pop()
                break

            else: 
                stack.append(a)
        return stack
