# quick sort 

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        # that means either the list is actually empty or it has one element in both cases we are going to return the whole list
        if len(nums) <= 1: 
            return nums

        mid = len(nums) // 2
        # also both of the left and right are recursive
        left = self.sortArray(nums[:mid]) # till the mid position
        right = self.sortArray(nums[mid:]) # starting from mid to last position

        merged = [] # the empty array to store the elements
        i = j = 0 # pointer index to go alongside the array 

        while i < len(left) and j < len(right): 
            # till we are working with the same size of the array the program is going to work, this is a limiter function for only those times when we encounter an array that has odd number elements
            if left[i] <=  right[j]: 
                merged.append(left[i])
                i += 1

            else: 
                merged.append(right[j])
                j += 1

        # i and j individually are the pointers where the loop actually broke so if there are any elements left after that the next two lines are going to help use append those elements in the final output
        merged.extend(left[i:]) # if the left partition contains any odd number of elements t is going to extend those in the final output
        merged.extend(right[j:]) # same for right side of the partition as well

        return merged