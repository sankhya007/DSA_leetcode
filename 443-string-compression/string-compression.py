# leetcode - text compression 

class Solution(): 
	def compress(self, chars): 

		# pointers 
		write = 0 
		read = 0 

		# is read == len(chars) means array ended
		while read < len(chars): 

			# element pick up
			current_char = chars[read]
			count = 0 

			# if element same
			while read < len(chars) and chars[read] == current_char:

				# increment 
				read += 1
				count += 1

			# element drop, write increment
			chars[write] = current_char
			write += 1

			# if more than one element, print element in array
			if count > 1: 
				# turn the count into string value(from int)
				for digit in str(count): 
					chars[write] = digit
					# write increment
					write += 1 

		# because array will have duplicate elements
		return write 


chars = ["a","a","b","b","c","c","c"]
sol = Solution()
print(sol.compress(chars))