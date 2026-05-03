class Solution:
    def diagonalSum(self, mat): 
        n = len(mat)
        total_sum = 0

        for i in range(n):
            total_sum += mat[i][i] # to get the normal diagonal 
            if i != n - 1 - i:
                total_sum += mat[i][n - 1 - i] # to get the reverse or the opposite diagonal 
                # write the values in pen and paper to undersnad better 

        return total_sum

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
solution = Solution()
print(solution.diagonalSum(mat))