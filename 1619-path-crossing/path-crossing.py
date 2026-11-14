class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)} # this is the position that we are going to start with 

        for direction in path: 
            if direction == "N": 
                y += 1
            if direction == "S": 
                y -= 1
            if direction == "E": 
                x += 1
            if direction == "W": 
                x -= 1

            if (x, y) not in visited: 
                visited.add((x, y))
            else: 
                return True

        return False 