from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        
        length = len(students)
        dq = deque(students)

        rest = length

        for sandwitch in sandwiches: 
            count = 0 

            while count < length and sandwitch != dq[0]: 
                current_element = dq.popleft()
                dq.append(current_element)
                count += 1 

            if sandwitch == dq[0]: 
                dq.popleft()
                rest -= 1

            else: 
                break 

        return rest