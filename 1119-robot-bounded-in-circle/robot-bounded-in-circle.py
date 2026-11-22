class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        location = [0,0]
        facing = "N" # initial face
        directions = ["N", "E", "S", "W"] # directions(clockwise)
        i = 0 # direction pointer

        for ch in instructions: 

            if ch == "R": 
                facing = directions[(i+1) % len(directions)]
                i += 1
            if ch == "L": 
                facing = directions[(i-1) % len(directions)]
                i -= 1

            if ch == "G":
                if facing == "N": 
                    location[1] += 1
                elif facing == "S": 
                    location[1] -= 1
                elif facing == "E": 
                    location[0] += 1
                elif facing == "W": 
                    location[0] -= 1

        # if it returns at initial, it'll make a circle no matter how manyes times we fuck with it
        if location == [0, 0]:  
            return True

        # if it does not moves ar all it'll stay at the same position
        if "G" not in instructions: 
            return True

        if facing != "N": 
            return True

        # anything else but those, FALSE!!
        return False