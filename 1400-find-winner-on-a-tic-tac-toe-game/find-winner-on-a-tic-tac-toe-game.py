class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        # if we have 9 moves that either means one one won at the last step, or no onw won, so if we hit this 1st of all we are going to follow the simulation that we are going to create, and if it does not matches then we return that the game was a draw
        total_moves = len(moves)

        win_conditions = [0] * 8
        '''
        this one is a little complicated. 
        there are 8 ways A or B can win the game
        1. rows fully clear, 3 possible ways 
        2. columns fully clear, 3 possible ways
        3. 2 diagonals

        we are going to go through the given moves and then for each one of the step we are going to seperate the rows nd cols

        the first 3 numbers in the win_condition will be denoted to rows
        later 3 to the columns
        and the last two will be for diagonals

        whichever number for the row we are going to add 1 to that position
        and for the column we will do the same but the position will be appended by 3 positions so that they ca stay at their designated location
        
        and for the diagonal numbers there can be two ways the numbers can be reppresented
        the positive diagonal (top-left to bottom-right): the locations for that diagonal are (0, 0), (1, 1), (2, 2) meaning rows == cols
        and the negitive diagonal (top-right to bottom-left): the locations can be (0, 2), (1, 1), (2, 0) meaning the rows + cols == 2

        when we hit 3 in any position in the win_condition that means someone has won the game
        '''

        # for each position jump by 2 so we stay at the line of the player itself and do not interfare with the other player
        # the even numbers - playber B 
        # the odd numbers - player A (because player A always starts)
        for move in range(len(moves)-1, -1, -2):
            row, col = moves[move] # reperate the values

            win_conditions[row] += 1
            win_conditions[col + 3] += 1 # adjusted 

            # as written in the example the last two spots are designated to the diagonals 
            # positive diagonal
            if row == col: 
                win_conditions[6] += 1
            # negitive diagonal
            if row + col == 2:
                win_conditions[7] += 1

            # if any of the position holds the count 3 meaning the game has been won by any of the players
            # if the move is in the even position it is B and if it is on the odd postion winner is A
            if any(count == 3 for count in win_conditions):
                return "B" if move & 1 else "A"
            '''
            here we are using bitwise and operator
            if the move is 1: binary of 1 is "001" so that becomes 1 & 1 which is True
            B will be at the positions (1, 3, 5, 7)
            A will be at the positions (0, 2, 4, 8)
            for all odd number the bitwise and operator will return True, meaning B wins 
            and for all the even operators it'll return False, meaning A wins
            '''

        # as mentioned in the explanation if total moves isequal to 9 even after bypassing through the simulation return Draw
        # and even after bypassing through the simulation if the length of the given moves is not 9 that means the player hs stopped playing before filling up all the squares 
        return "Draw" if total_moves == 9 else "Pending"