class Solution:
    def isSafe(self, i, j, n, m): 
        return 0 <= i < n and 0 <= j < m
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        elapsedTime = 0 
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while True: 
            changed = False
            has_fresh = False
            for i in range(n): 
                for j in range(m): 
                    if grid[i][j] == 1: 
                        has_fresh = True
                    if grid[i][j] == elapsedTime + 2: 
                        for direction in directions: 
                            x = i + direction[0]
                            y = j + direction[1]
                            if self.isSafe(x, y, n, m) and grid[x][y] == 1: 
                                grid[x][y] = elapsedTime + 3
                                changed = True 
            if not changed: 
                return -1 if has_fresh else elapsedTime
            elapsedTime += 1