class Solution:
    def judgeCircle(self, moves: str) -> bool:
        current = [0, 0]

        for move in moves: 
            if move == "U": 
                current[1] += 1
            elif move == "D": 
                current[1] -= 1
            elif move == "R": 
                current[0] += 1
            elif move == "L": 
                current[0] -= 1
            
        if current != [0, 0]: 
            return False
        
        return True
        