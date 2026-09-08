class Solution(): 
	def getHint(self, secret, guess): 

		bulls = 0 
		cows = 0 

		# storage
		secret_storage = {}
		guess_storage = {}

		# checking if the position of the number is exact 
		for i in range(len(secret)): 
			if secret[i] == guess[i]: 
				bulls += 1
			# adding up the numbers and seeing how many are there in each
			else: 
				secret_storage[secret[i]] = secret_storage.get(secret[i], 0) + 1
				guess_storage[guess[i]] = guess_storage.get(guess[i], 0) + 1
			# this is hoe the output will look like

			# select_storage 
			# "1" - 1
			# "7" - 1
			# "8" - 1

			# guess_storage
			# "8" - 1
			# "1" - 1
			# "7" - 1

		# checking how many numbers in the storage actually matches 
		for num in secret_storage: 
			if num in guess_storage: 
				# giving out the matching number(one by one addition)
				cows += min(secret_storage[num], guess_storage[num])

		# intended format (as per question)
		return str(bulls) + "A" + str(cows) + "B"