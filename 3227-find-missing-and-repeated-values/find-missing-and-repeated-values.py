class Solution: 
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        seen = set()
        repeated = 0 
        length = len(grid)

        # find repeated to go through all the elemts in grid
        for row in grid: 
            for element in row: 
                if element in seen: 
                    repeated = element
                seen.add(element)

        # get max lenght of the grid 
        for missing in range(1, length * length + 1): 
            if missing not in seen: 
                return [repeated, missing]