from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        
        length = len(students)
        dq = deque(students)

        rest = length 
        # this is the variable that is denoting how many students we have left in the stack itself, at the start it will be the same as teh length of the array

        for sandwitch in sandwiches: 
            count = 0 

            # while te 1st element is not matching we are goign to keep on popping that element from there and appending that at the last and everytime the count is going to go up, the count has to be lower than the actual length because if not that means no one will get anything to eat at all
            # and also make sure that they do not match then we pop
            while count <= length and sandwitch != dq[0]: 
                current_element = dq.popleft()
                dq.append(current_element)
                count += 1 # the count goes up everytime

            # if the number matches then we are just going to pop that elemnt and then negate one for the rest because that is the number of students that we have left out
            if sandwitch == dq[0]: 
                dq.popleft()
                rest -= 1

            # eeh whatever
            else: 
                break 

        return rest