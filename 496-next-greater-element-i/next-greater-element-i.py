class Solution(): 
	def nextGreaterElement(self, nums1, nums2):
		# the fun part in this is that we are going to fuck around with the nums2 till the end lol 
		stack = [] # just to store the numbers 
		next_greater = {} # here we are going to store the index of the nummebrs which well see in the nums 2 
		for num in nums2: # loop in nums2 array 
			while stack and num > stack[-1]: # here we are comparing it to the top most element in the stack 
				prev = stack.pop() # the stack will pop the previous element because the loop is running on the next element and till then before that number gets appended in the stack it will have the last/prev elemnt in the top most position
				next_greater[prev] = num # here we are storing the prev meanign the topmost elemnt of the stack to the next biggest number so then it wil have that value assigned in it 
			stack.append(num) # no matter what the number will be appended in the stack till the array ends and then it will be popped out of the stack and the left overs will be allocated -1 indicating that tehy do not have any numbers greater than them 

		# now too assign the -1 to the left overs
		for num in stack: # meaning it is going to go through the left over onces that we were unable to pop because of the condition 
			next_greater[num] = -1 #assign -1 as instructed 
		
		return [next_greater[num] for num in nums1] # so what this is going to do is it is just gonna loop through the numbers in the nums1 array and then present them as next_greater[1] (assuming the nums1 has the number 1) and do that for all of the numbers and then as return we would get the numbers assigned in the next_greater in an array, for the assigned numbers it will return the numbe and for the numbers which did not have the greater number to their right it'll give -1 in the array
