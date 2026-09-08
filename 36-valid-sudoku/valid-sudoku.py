# valid sudoku - leetcode 

class Solution(): 
	def isValidSudoku(self, board): 

		# checking rows one by one
		for row in board: 
			# for each rows there will be a set
			seen = set()

			# scan though each number in the rows
			for num in row: 
				# if not number skip 
				if num == ".": 
					continue

				# if in seen then say false because invalid
				if num in seen: 
					return False

				# if not seen then add
				seen.add(num)

		# checking columns one by one {0,1,2,3...,9}
		for col in range(9): 

			# make a new set for each of the rows
			seen = set()

			# same as cols but for each row in the col
			for row in range(9): 
				# for specific position in the table(it is important to specify the row and the col of the board to go through the numbers properly)
				num = board[row][col]

				if num == ".": 
					continue

				if num in seen: 
					return False

				seen.add(num)

		# start at 0, go up-to 9 by jumping 3 block each times(for both rows and cols)
		for box_row in range(0, 9, 3): 
			for box_col in range(0, 9, 3): 

				seen = set()

				# box_row = 3 -> range(3,6) = 3,4,5
				# box_col = 6 -> range(6,9) = 6,7,8
				# so then we are checking for
				#         columns
				#         6  7  8
				#       ┌─────────┐
				# row 3 │ ■  ■  ■ │
				# row 4 │ ■  ■  ■ │
				# row 5 │ ■  ■  ■ │
				#       └─────────┘
				for row in range(box_row, box_row + 3): 
					for col in range(box_col, box_col + 3): 

						num = board[row][col]
						# here we also have to specify the exact location of the number that we are searching for, because it does not have a gradual increase

						if num == ".": 
							continue

						if num in seen: 
							return False

						seen.add(num)

		return True

