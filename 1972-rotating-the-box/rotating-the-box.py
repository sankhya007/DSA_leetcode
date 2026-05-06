class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid) 
        n = len(boxGrid[0])

        for row in boxGrid: 
            empty = n - 1 # right most position of the row

            for j in range(n - 1, -1, -1): 
                if row[j] == '*': 
                    empty = j - 1
                elif row[j] == '#': 
                    row[j] = '.'
                    row[empty] = '#'
                    empty -= 1
                
        res = [[None] * m for _ in range(n)]

        for i in range(m): 
            for j in range(n): 
                res[j][m - 1 - i] = boxGrid[i][j]

        return res

            