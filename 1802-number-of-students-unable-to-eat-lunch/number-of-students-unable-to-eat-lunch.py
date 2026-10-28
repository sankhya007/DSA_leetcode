class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        length = len(students)
        # change the students into a queue because that is what that we are going to change
        q = deque(students)

        rest = length

        for sandwitch in sandwiches: 
            count = 0 

            # this has to be a concurrent phenomena thats why this has to been on a loop
            while count < length and sandwitch != q[0]: 
                # no match we have all students lest in stack
                current = q.popleft()
                q.append(current)
                count += 1 

            if sandwitch == q[0]: 
                # sandwitch match we remove one student form rest
                q.popleft()
                rest -=1  

            else: 
                break 

        return rest 