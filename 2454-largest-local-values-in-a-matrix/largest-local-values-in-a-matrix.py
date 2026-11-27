class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        # it is square matrix and the len is n
        # no of rows will ne n and cols will also be n 

        n = len(grid)
        answer = [[0] * (n - 2) for _ in range(n - 2)]

        for row in range(n-2): 
            for col in range(n-2): 
                answer[row][col] = max(grid[x][y]
                    for x in range(row, row+3)
                    for y in range(col, col+3)
                    )
        return answer