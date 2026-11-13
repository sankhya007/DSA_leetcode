class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        valid_triangle = [[1]]

        if numRows == 1: 
            return valid_triangle

        for i in range(1, numRows): 
            prev_row = valid_triangle[-1]
            row = [1] # because the 1st element will always be 1
            for j in range(1, i): 
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1) # because the last element of the row will also always be 1
            valid_triangle.append(row)

        return valid_triangle