class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        # because now row
        if rowIndex == 0: 
            return [1]

        # 1st element
        curRow = [1]

        # for only the last index
        prevRow = self.getRow(rowIndex - 1)

        for i in range(1, rowIndex): 
            curRow.append(prevRow[i - 1] + prevRow[i])

        # last element
        curRow.append(1)

        return curRow