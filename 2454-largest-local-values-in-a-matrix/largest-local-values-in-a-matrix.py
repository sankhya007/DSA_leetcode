class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        # it is square matrix and the len is n
        # no of rows will ne n and cols will also be n 

        n = len(grid)
        answer = [[0] * (n - 2) for _ in range(n - 2)]

        # this loop if for the answer 2d array that we are running to determine what number will occupy that specific position
        for row in range(n-2): 
            for col in range(n-2): 
                # and this loop will look for the each eleemnt in the row indivisual to their column and set out the max number and at the end we atteond that to the result array
                answer[row][col] = max(grid[x][y]
                    for x in range(row, row+3)
                    for y in range(col, col+3)
                    )
        return answer