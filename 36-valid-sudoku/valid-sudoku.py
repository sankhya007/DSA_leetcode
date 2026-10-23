class Solution(): 
    def isValidSudoku(self, board):

        for row in board: 
            seen = set()
            for num in row: 
                if num in seen: 
                    return False
                elif num == ".": 
                    continue
                seen.add(num)

        for col in range(9): 
            seen = set()
            for row in range(9): 
                num = board[row][col]
                
                if num in seen: 
                    return False
                elif num == ".": 
                    continue
                seen.add(num)

        for box_row in range(0, 9, 3): 
            for box_col in range(0, 9, 3): 
                seen = set()

                for row in range(box_row, box_row + 3): 
                    for col in range(box_col, box_col + 3): 
                        num = board[row][col]

                        if num in seen: 
                            return False
                        elif num == ".": 
                            continue
                        seen.add(num)

        return True
                