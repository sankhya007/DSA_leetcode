class Solution:
    def transpose(self, matrix): 
        rows = len(matrix)
        cols = len(matrix[0]) # this is to get the length of the 2d array we are saying a matrix so the number of elemets in the array will be the length of the rows and the number of elements inside the elemts will be the columns

        transposed = [[0] * rows for _ in range(cols)] # this is to intercgange the length of the rows and the columns

        for i in range(rows): 
            for j in range(cols):
                transposed[j][i] = matrix[i][j] # just adding the values in the existing matrix(transposed)

        return transposed

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
print(solution.transpose(matrix))

        