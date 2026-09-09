class Solution(): 
	def leastBricks(self, walls): 

		edge_count = {}

		for row in walls: 
			# count each of the rows
			position = 0 

			for brick in row[:-1]: 
				# count each of the bricks(leave the last one, because all of it will be an edge)
				position += brick
				# increment value per brick

				edge_count[position] = edge_count.get(position, 0) + 1
				# incremental edge count for all bricks in each rows

			max_edges = max(edge_count.values()) if edge_count else 0
				# for the row that has the max count of edges


		return len(walls) - max_edges
		# return the opposite of edge count