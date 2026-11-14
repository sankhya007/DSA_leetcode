class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        seen = set()
        repeated = 0 
        length = len(grid) # grid is a square matrix to nums in row and the len of grid will always be the same 

        for rows in grid: 
            for num in rows:
                if num in seen: 
                    repeated = num  
                seen.add(num)

        for missing in range(1, length * length + 1): 
            if missing not in seen:
                return [repeated, missing] 
