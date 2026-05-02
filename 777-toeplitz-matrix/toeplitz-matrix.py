class Solution:
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]: # this is is the wway to get the next element in the same diagonal of the matrix so (0, 0) to (1, 1) if not same return False
                    return False

        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
solution = Solution()
print(solution.isToeplitzMatrix(matrix))
