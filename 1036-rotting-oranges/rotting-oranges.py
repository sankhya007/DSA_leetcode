class Solution: 
    def isSafe(self, i, j, n, m): 
        return 0 <= i < n and 0 <= j < m # are in boundary
    def orangesRotting(self, grid): 
        n = len(grid)
        m = len(grid[0])
        elapsedTime = 0 
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while True: 
            has_fresh = False
            changed = False # change de default for every loop 
            for i in range(n): 
                for j in range(m): 
                    if grid[i][j] == 1: # find the fresh onces 
                        has_fresh = True
                    if grid[i][j] == elapsedTime + 2: # are able to rot coz atleast 2
                        for direction in directions: 
                            x = i + direction[0]
                            y = j + direction[1] # 4 direction contamination 
                            if self.isSafe(x, y, n, m) and grid[x][y] == 1: # rotting done still some left fresh 
                                grid[x][y] = elapsedTime + 3 # matter elapsed time 
                                changed = True
            if not changed: 
                return -1 if has_fresh else elapsedTime # if fhesh return -1 else time 
            elapsedTime += 1