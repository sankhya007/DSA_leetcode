class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = [[1]]
        
        if rowIndex == 0: 
            return triangle[-1]

        for i in range(rowIndex+1): 
            previous = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(previous[j-1] + previous[j])
            row.append(1)
            triangle.append(row)

        return triangle[-1]