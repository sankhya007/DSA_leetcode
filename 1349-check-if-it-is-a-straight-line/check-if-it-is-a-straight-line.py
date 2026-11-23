class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for i in range(2, len(coordinates)): 
            x3, y3 = coordinates[i] #3rd point, for the rest of the coordinates
            if (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1): 
                return False
        
        return True