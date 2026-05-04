class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # transpose the matrix, but do nto create a new one, transpose the existing one
        for i in range(n): 
            for j in range(i, n): # here we are not using both rows and the cols because then it would be hard to keep the problem going in the one triangular part of the matrix, this is done to make sure only one triangular part is getting used 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n): 
            matrix[i].reverse()
            # reversing all the rows in the matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
solution.rotate(matrix)
print(matrix)

