class Solution():
    def rowAndMaximumOnes(self, mat): 
        max_ones = 0 
        row_index = 0

        for i in range(len(mat)):
            current_ones = sum(mat[i])
            if current_ones > max_ones: 
                max_ones = current_ones 
                row_index = i

        return [row_index, max_ones]

mat = [[0,0],[1,1],[0,0]]
solution = Solution()
print(solution.rowAndMaximumOnes(mat))

            