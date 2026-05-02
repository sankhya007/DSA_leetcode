class Solution:
    def setZeroes(self, matrix): 
        rows = len(matrix)
        cols = len(matrix[0]) # initialize the length
        zero_rows = set()
        zero_cols = set() # here we are adding the storage for the location of the rows and cols so that they gat added in a set and there is no duplicate so then the loop do not have to go through unneeded steps 

        for i in range(rows): # this step is done to identify the positions where we can see the 0 
            for j in range(cols):
                if matrix[i][j] == 0: 
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(rows): # this step is done to make all the vals thats we have in the cols and rows connected to that position zeros indivisually 
            for j in range(cols):
                if i in zero_rows or j in zero_cols: # here the "or" is really important 
                    matrix[i][j] = 0

        return matrix 

matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
print(solution.setZeroes(matrix))