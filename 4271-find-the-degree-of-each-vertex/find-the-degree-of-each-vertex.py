class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 1: 
            return matrix[0]
        
        array = []
        for value in matrix: 
            total = 0 
            for ch in value: 
                total += ch
            array.append(total)
        return array 