class Solution:
    def numIslands(self, grid):
        if not grid: 
            return 0 # this is to see if the array is empty or nah 

        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0 # initialize vals 

        def dfs(r, c): 
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0': 
                # r less than 0 or mroe than rows and c less than 0 or more than cols is out of bound meaning it does not exist in the grid thats why we can not count then if we get that value 
                # simillerly if it is 0 then there is nothing for us to see in there 
                return 
            
            grid[r][c] = '0' # this is marking all the visited cells as 0 so then we do not have to visit there anymore in the future
            
            # this is done to check the neighbouring cells if they are 1 or no if any of them are 1 then it wil lbe a part of the island that we are calculating and if not then it is going to be indivisuial island by itself
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down 
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right

        for i in range(rows): 
            for j in range(cols):
                if grid[i][j] == '1': 
                    num_islands += 1 # this is to count the number of 1s 
                    dfs(i, j) # depth 1st search call, if we didnt have called this then it would have been like counting the elements in the sparce matrix and that is not what we want
        
        return num_islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
solution = Solution()
print(solution.numIslands(grid))
