class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid) 
        n = len(boxGrid[0])

        for row in boxGrid: 
            empty = n - 1 # right most position of the row so when we are goin to rotate that 90 degrees this is going to be the bottom of the box and the index of the bottom of the box is this 

            for j in range(n - 1, -1, -1): 
                if row[j] == '*': 
                    empty = j - 1 # because the stone can not pass the obstacle that is why we are going decrease the length of the end of the box 
                elif row[j] == '#': 
                    row[j] = '.'
                    row[empty] = '#'
                    empty -= 1 # stone comes down , the position becomes empty and then the empty space index decreses by 1
                
        res = [[None] * m for _ in range(n)] # making a clear array with the rows and cols inversed as the standerd one 

        for i in range(m): 
            for j in range(n): 
                res[j][m - 1 - i] = boxGrid[i][j] # placing the values from the box to the res , the changed values 

        return res

            