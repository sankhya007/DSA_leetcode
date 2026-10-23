class Solution(): 
    def isValidSudoku(self, board):

        # selct a row 
        for row in board: 
            seen = set()
            # go left to right
            for num in row: 

                # check if . or not
                # also if exist or no
                if num in seen: 
                    return False
                elif num == ".": 
                    continue
                seen.add(num)

        # select a col
        for col in range(9): 
            seen = set()
            # go top to bottom
            for row in range(9): 
                num = board[row][col]
                
                # check if . or not
                # also if exist or no
                if num in seen: 
                    return False
                elif num == ".": 
                    continue
                seen.add(num)

        # select a 3x3 box 
        for box_row in range(0, 9, 3): 
            for box_col in range(0, 9, 3): 
                seen = set()

                # go through each of ther numbers
                for row in range(box_row, box_row + 3): 
                    for col in range(box_col, box_col + 3): 
                        num = board[row][col]

                        # check if . or not
                        # also if exist or no
                        if num in seen: 
                            return False
                        elif num == ".": 
                            continue
                        seen.add(num)

        return True
                